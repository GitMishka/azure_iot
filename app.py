from flask import Flask, jsonify
from threading import Thread
import time

app = Flask(__name__)

class IoTDevice:
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        while self.is_running:
            print("IoT device is running...")
            time.sleep(1)

    def stop(self):
        self.is_running = False

device = IoTDevice()

@app.route('/start', methods=['GET'])
def start_device():
    if not device.is_running:
        Thread(target=device.start).start()
    return jsonify({"status": "Device started"})


@app.route('/stop', methods=['GET'])
def stop_device():
    if device.is_running:
        device.stop()
    return jsonify({"status": "Device stopped"})

if __name__ == '__main__':
    app.run(port=5000)
