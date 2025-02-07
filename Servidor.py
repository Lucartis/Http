from flask import Flask, request, Response, jsonify
import time
import json

app = Flask(__name__)

current_position = {"lat": None, "lng": None}

@app.route('/sensorData', methods=['POST'])
def sensor_data():
    global current_position
    data = request.json  # e.g., {"lat": 40.0, "lng": -74.0}
    # Update position
    current_position = data
    print(f"Received data: {data}")
    return "OK", 200

@app.route('/position', methods=['GET'])
def get_position():
    return jsonify(current_position)

@app.route('/events', methods=['GET'])
def stream_events():
    def event_stream():
        while True:
            time.sleep(1)
            yield f"data: {json.dumps(current_position)}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    import sys
    print("Usage: python Servidor.py [5000 o 5001]")
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(debug=True, port=port)
