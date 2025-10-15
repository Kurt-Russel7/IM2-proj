from flask import Flask, render_template, request                                     

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route("/profile", methods = ["POST"])
def profile():
    Fname = request.form['FirstName']
    Lname = request.form['LastName']
    sex = request.form['sex']
    status = request.form['status']
    Loc = request.form['location']
    return render_template('profile.html',Fname= Fname,Lname = Lname, sex = sex, status = status, Loc = Loc)

if __name__ == '__main__':
    app.run(debug = True)  

