'''
I need create cycle for img
'''


from flask import Flask, render_template
import os

app = Flask(__name__)
picFolder = os.path.join('static', 'Moto', '1', '2', '3')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def some_HTML():
    return render_template('1st.html')


@app.route('/template')
def templatr():
    return render_template('index.html')


app.run('localhost')