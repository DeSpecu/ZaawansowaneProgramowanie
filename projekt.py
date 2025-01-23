from flask import Flask, jsonify, request
import torch
from PIL import Image
import requests
from io import BytesIO
import uuid
import threading
import queue
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

task_results = {}
task_queue = queue.Queue()

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_humans(image, task_id, type):
    if type == "url":
        response = requests.get(image)
        image_processed = Image.open(BytesIO(response.content))
    elif type == "file":
        image_processed = Image.open(image)
    elif type == "upload":
        image_processed = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image))
        
    try:
        results = model(image_processed)
        detections = results.pandas().xyxy[0]
        person_count = len(detections[detections['name'] == 'person'])
        task_results[task_id] = {"status": "completed", "person_count": person_count}
    except Exception as e:
        task_results[task_id] = {"status": "error", "error": str(e)}

def worker():
    while True:
        task_id, image, type = task_queue.get()
        if task_id is None:
            break
        detect_humans(image, task_id, type)
        task_queue.task_done()

@app.route('/detect_url', methods=['GET'])
def detect_url():
    image_url = request.args.get('image_url')
    if not image_url:
        return jsonify({"error": "Brak parametru image_url"}), 400
    
    task_id = str(uuid.uuid4())
    task_results[task_id] = {"status": "processing"}
    task_queue.put((task_id, image_url, "url"))
    
    return jsonify({"task_id": task_id})

@app.route('/detect_file', methods=['GET'])
def detect_file():
    image_path = request.args.get('image_path')
    if not image_path:
        return jsonify({"error": "Brak parametru image_path"}), 400
    
    task_id = str(uuid.uuid4())
    task_results[task_id] = {"status": "processing"}
    task_queue.put((task_id, image_path, "file"))
    
    return jsonify({"task_id": task_id})

@app.route('/detect_upload', methods=['GET','POST'])
def detect_upload():
    if 'file' not in request.files:
        return jsonify({"error": "Brak przesłanego pliku"}), 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    task_id = str(uuid.uuid4())
    task_results[task_id] = {"status": "processing"}
    task_queue.put((task_id, filename, "upload"))
    
    return jsonify({"task_id": task_id})

@app.route('/task_status', methods=['GET'])
def task_status():
    task_id = request.args.get('task_id')
    if not task_id or task_id not in task_results.keys():
        return jsonify({"error": "Nieznane task_id"}), 400
    
    return jsonify(task_results[task_id])

if __name__ == '__main__':
    num_workers = 2  
    threads = []
    for _ in range(num_workers):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)
    # for i in range(1000):
    #     task_id = str(uuid.uuid4())
    #     task_queue.put((task_id, r"C:\Users\szymk\Downloads\th.jpg", "file"))
    #     task_results[task_id] = {"status": "processing"}
    #     if i%100 == 0:
    #         print("TASK ID:  "+task_id)
    app.run(debug=True)