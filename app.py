from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id' : 1,
        'title': 'Data Analyst',
        'Location': 'Kenya',
        'Salary': 'Ksh. 200,000'
    },
    {
        'id' : 2,
        'title': 'Data Engineer',
        'Location': 'Sudan',
    },
    {
        'id' : 3,
        'title': 'Data Scientist',
        'Location': 'Tanzania',
        'Salary': 'Ksh. 900,000'
    }
    ]

@app.route("/")
def hello_world():
    return render_template('index.html', jobs=JOBS, company_name='Jecinta')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)