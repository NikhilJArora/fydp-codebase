from flask import *
import pandas as pd

app = Flask(__name__)

data_path = '/Users/nikhilarora/data/fydp/pi_data/output.csv'

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/tables")
def show_tables():

    ps_data = pd.read_csv(data_path)
    #return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
    #titles = ['na', 'Female surfers', 'Male surfers'])
    return render_template(
                            'view.html',
                            table=get_new_html()
                        )

@app.route("/poll_stats")
def system_info(): # you need an endpoint on the server that returns your info...
    return get_new_html()

def get_new_html():
    return pd.read_csv(data_path).to_html(classes='states', index=False)


if __name__ == "__main__":
    app.run(debug=True)
