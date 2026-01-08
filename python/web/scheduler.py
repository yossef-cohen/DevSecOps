from flask import Flask, jsonify
from flask import request
import heapq
import json

app = Flask(__name__)

heap = []
heapq.heapify(heap)

a = {"title": "Sync", "start": 1400, "duration": 60}

@app.route("/schedule" , methods=['POST'])
def scheduler_root():
    global heap
    title = request.get_json().get("title")
    NewStart = request.get_json().get("start")
    duration = request.get_json().get("duration")
    NewEnd = NewStart + duration
    
    if not title or not NewStart or not duration:
        return jsonify({"Bad Request\n"}), 400

    for task in heap:
        if (NewStart < task[1]) and (NewEnd > task[0]):
            return jsonify({"Bad Request\n"}), 400
        
    heapq.heappush(heap, (NewStart, duration+NewStart, title))
    print(heap)
    return jsonify({"Task scheduled: Title: {title}, start_time: {NewStart}, end_time: {NewEnd}\n"}), 201

@app.route("/next", methods=['GET'])
def get_next_task():
    global heap
    if not heap:
        return jsonify({"Not Found\n"}), 404
    return jsonify({"next_task": heap[0]}), 200

@app.route("/complete", methods=['POST'])
def complete_task():
    global heap
    if not heap:
        return jsonify({"Not Found\n"}), 404
    heapq.heappop(heap)
    return jsonify({"OK\n"}), 200

app.run()