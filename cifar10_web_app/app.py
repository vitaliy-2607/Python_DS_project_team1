from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', os=os)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join('static', 'uploads', filename))
    return 'Image successfully uploaded!'


if __name__ == '__main__':
    app.run(debug=True)