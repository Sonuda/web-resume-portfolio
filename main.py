from flask import Flask, render_template, send_from_directory


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/download_resume')
def download_resume():
    # Send the file from the 'static' folder with attachment disposition
    return send_from_directory('static', 'files/Kashish_resume_05.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
