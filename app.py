from flask import Flask, render_template, request

app = Flask(__name__)

data = {
    "ключ1": "значение1",
    "ключ2": "значение2",
    "ключ3": "значение3"
}

@app.route('/', methods=['GET', 'POST'])
def search_replace():
    if request.method == 'POST':
        search_key = request.form['search_key']
        replace_value = request.form['replace_value']
        if search_key in data:
            data[search_key] = replace_value
        
        return render_template('index.html', data=data)
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()