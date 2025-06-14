import os
from dotenv import load_dotenv
from steam_web_api import Steam
from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

load_dotenv()
user_friends ={}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search',methods= ["GET","POST"])
def search():
    global user_friends
    if request.method =="POST":
        user_id = request.form.get("q")
        steam = Steam(os.environ['STEAM_API_KEY'])
        user_friends = steam.users.get_user_friends_list(user_id)
        print(user_friends)
        return redirect(url_for("user_friends"))
    return redirect(url_for('home'))

@app.route("/user_friends")
def user_friends():
    number_of_friends = len(user_friends["friends"])
    return render_template("user_data.html",friends = user_friends["friends"],no_player = number_of_friends)


if __name__ == "__main__":
    app.run(debug=True)


