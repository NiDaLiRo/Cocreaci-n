from flask import Flask, render_template
from data_viisualization import generate_seaborn_plot
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/charts')
def charts():  # put application's code here
    generate_seaborn_plot()
    return render_template('charts.html')

if __name__ == '__main__':
    app.run()
