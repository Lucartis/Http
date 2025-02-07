import requests
import time

url = "http://127.0.0.1/sensorData"
simulated_data = []
lat, lng = 40.0, -74.0
for _ in range(10):
    simulated_data.append({"lat": lat, "lng": lng})
    lat += 0.0001
    lng += 0.0001

for point in simulated_data:
    requests.post(url, json=point)
    time.sleep(1)
