from flask import Flask, request, render_template, jsonify
import datetime
from google_sheet_api import write_data_to_sheet
import pytz
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ip')
def get_ip_address():
    forwarded_ip = request.headers.get('X-Forwarded-For')

    if forwarded_ip:
        ip_address = forwarded_ip.split(',')[0]
    else:
        ip_address = request.remote_addr

    ist = pytz.timezone('Asia/Kolkata')
    timestamp = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    write_data_to_sheet(ip_address, timestamp)

    return jsonify({'ip': ip_address, 'timestamp': timestamp})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
