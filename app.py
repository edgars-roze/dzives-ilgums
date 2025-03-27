from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('dataset.csv', index_col='Country')
df = df.sort_values(by=['Year'])
df = df[~df.index.duplicated(keep='first')]

@app.route('/', methods=['GET', 'POST'])
def index():
	v_figsize=(9, 6.7)
	v_kind = 'pie'

	if request.method == 'POST':
		if request.form['button'] == 'H. stabiņu':
			v_kind = 'barh'
		elif request.form['button'] == 'V. stabiņu':
			v_figsize=(9, 9)
			v_kind = 'bar'
		#elif request.form['button'] == 'Histogramma':
		#	ploo = plt.hist(x=df['Life_expectancy'])
		#	plt.tight_layout()

		#	chart = ploo.get_figure()
		#	chart.savefig('static/image/chart.png')
		#	return render_template('index.html')

	ploo = df.groupby('Region').mean().plot(figsize=v_figsize, legend=False, kind=v_kind, xlabel='', y='Life_expectancy', ylabel='', title='Dzīves ilgums pēc reģiona')

	plt.tight_layout()

	chart = ploo.get_figure()
	chart.savefig('static/image/chart.png')
	return render_template('index.html')

@app.route('/download')
def download():
	return send_file('dataset.csv', as_attachment=True)
