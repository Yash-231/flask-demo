from flask import send_from_directory, abort, Flask

app = Flask(__name__)

@app.route('/get-file/<path:filename>')
def get_file_path(filename):
    try:
        return send_from_directory("C:/Users/yashs/Desktop/python_backend/flask/download-files/static", filename, as_attachment=False)
    except FileNotFoundError:
        return abort(404)

@app.route('/get-file/<filename>')
def get_file_name(filename):
    try:
        return send_from_directory("C:/Users/yashs/Desktop/python_backend/flask/download-files/static/client", filename, as_attachment=True)
    except FileNotFoundError:
        return abort(404)

if __name__ == '__main__':
    app.run(debug=True)