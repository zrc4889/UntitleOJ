from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
run_path = os.path.abspath('')

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':

        f = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(path)
        filename = secure_filename(f.filename);

        cmd = 'g++ ' + run_path + '\\upload\\' + filename
        os.system(cmd)
        os.system('.\\a.exe' + ' < ' + run_path + '\\problem\\1\\1.in' + ' > ' + run_path + '\\record\\1\\1.out')

        return 'file uploaded successfully'
    else:
        return render_template('upload.html')
    
if __name__ == '__main__': 
    app.run(debug=True)