from flask import app, render_template, request, redirect, url_for
from .model import YourModelClass

model_instance = YourModelClass()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form['input_data']
        result = model_instance.process_data(input_data)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)