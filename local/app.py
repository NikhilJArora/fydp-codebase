from flask import *
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')

    suggestions_list = []

    if text:
        r = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=ru&q={}&gl=in'.format(text))

        soup = BeautifulSoup(r.content, 'lxml')

        suggestions = soup.find_all('suggestion')

        for suggestion in suggestions:
            suggestions_list.append(suggestion.attrs['data'])


@app.route("/tables")
def show_tables():
    data_path = '/Users/nikhilarora/data/fydp/pi_data/output.csv'
    ps_data = pd.read_csv(data_path)
    #return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
    #titles = ['na', 'Female surfers', 'Male surfers'])
    return render_template('view.html',tables=[ps_data.to_html(classes='states')],
    titles = ['na', 'Parking Spots'])

if __name__ == "__main__":
    app.run(debug=True)
