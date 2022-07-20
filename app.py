from flask import Flask, render_template, redirect, request, send_file
import pyqrcode
from pyqrcode import QRCode
import png

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST': # if file exist etc.
        url = request.form.get("url")
        qr = pyqrcode.create(url)
        a = qr.png("qrcode.png", scale=8)
        return redirect("/download")
    return render_template("index.html")

@app.route("/download",methods=['GET','POST'])
def download():
    return (send_file('/Flask/qrcode.png',attachment_filename='qrcode.png'))


if __name__ == '__main__':
    app.run(debug=True)
