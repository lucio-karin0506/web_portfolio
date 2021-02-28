from flask import Flask, render_template

app = Flask(__name__)

stu_data = {
    1: {"name": "슈퍼맨", "score": {"국어": 90, "수학": 65}},
    2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75}}
}

@app.route('/')
def index():
    return render_template('index.html', template_students=stu_data)

@app.route('/student/<int:id>')
def stu(id):
    return render_template('student.html',
            template_name=stu_data[id]['name'],
            template_score=stu_data[id]['score'])

if __name__ == '__main__':
    app.run(debug=True)