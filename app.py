from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'Location': 'Bengaluru, India',
  'Salary': 'RS. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scieentist',
  'Location': 'Delhi, India',
  'Salary': 'RS. 15,00,000'
}, {
  'id': 3,
  'title': 'Full-stack Developer',
  'Location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'Location': 'San Francisco, USA',
  'Salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
