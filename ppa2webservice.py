from flask import Flask, render_template, request, redirect, escape
from ppa1 import bmi, bmi_calculator, distance, log_bmi, log_distance

app = Flask(__name__)

@app.route('/calcbmi', methods=['POST'])
def calc_bmi() -> str:
    feet = request.form['feet']
    inches = request.form['inches']
    pounds = request.form['pounds']
    title = 'Here are your results:'
    results = bmi(feet, inches, pounds)
    log_bmi(feet, inches, pounds, bmi_calculator(feet, inches, pounds))
    return render_template('bmi_results.html', the_feet=feet, the_inches=inches, the_pounds=pounds, the_title=title, the_results=results,)


@app.route('/calcdistance', methods=['POST'])
def calc_distance() -> str:
    x1 = request.form['x1']
    x2 = request.form['x2']
    y1 = request.form['y1']
    y2 = request.form['y2']
    title = 'Here are your results:'
    results = distance(x1, x2, y1, y2)
    log_distance(x1, x2, y1, y2, results)
    return render_template('distance_results.html', the_x1=x1, the_x2=x2, the_y1=y1, the_y2=y2, the_title=title, the_results=results,)


@app.route('/bmi')
def get_bmi_table() -> 'html':
    contents = []
    with open('bmi.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = {'Feet', 'Inches', 'Pounds', 'Result', 'Timestamp'}
    return render_template('log.html', the_title='BMI Log', the_row_titles=titles, the_data=contents,)


@app.route('/distance')
def get_distance_table() -> 'html':
    contents = []
    with open('distance.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = {'X1', 'X2', 'Y1', 'Y2', 'Result', 'Timestamp'}
    return render_template('log.html', the_title='Distance Log', the_row_titles=titles, the_data=contents,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='PPA2 Entry Page')


if __name__ == '__main__':
    app.run(debug=True)
