from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return "Success"
    else:
        return str(socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
