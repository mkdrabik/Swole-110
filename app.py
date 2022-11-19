from flask import Flask, render_template, request
from helpers import workout

app: Flask = Flask(__name__)
workout_list: list[workout] = []


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create-workout', methods=["GET", "POST"])
def create_workout():
    if request.method == "POST":
        global workout_list
        
        goal: str = request.form['goal']
        type: str = request.form['workout']
        print(type)


        new_workout: workout = workout(goal, type)
        workout_list.append(new_workout)


        return render_template("success.html", title=goal, description=type)
    return render_template("create-workout.html")


@app.route('/view-todo-list', methods=["GET", "POST"])
def view_todo_list():
   
    return render_template('view-list.html', workout_list=workout_list)



if __name__ == '__main__':
    app.run(debug=True)
