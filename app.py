from flask import Flask, render_template, jsonify
from database import fetch_jobs

app = Flask(__name__)


def get_jobs():
    jobs = fetch_jobs()
    return jsonify(jobs)

@app.route("/")
def hello_world():
    JOBS = get_jobs()
    return render_template('index.html', jobs=JOBS, company_name='Jecinta')

@app.route("/api/jobs")
def list_jobs():
    JOBS = get_jobs()
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)