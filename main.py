import os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
pathh = 'static/img'

os.makedirs(pathh, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return redirect(request.url)
        file = request.files['photo']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file.save(os.path.join(pathh, filename))
            return redirect(url_for('upload_photo', filename=filename))

    filename = request.args.get('filename')

    return render_template('upload.html', filename=filename)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
