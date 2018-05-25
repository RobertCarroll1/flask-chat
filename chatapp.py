import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
messages=[]
banned_words = [
        "Poo",
        "bird",
        "word"
        ]
messages = []
        
      
@app.route("/")
def get_index():
    return render_template("index.html")
    
@app.route("/login")
def do_login():
    username = request.args["username"]
    return redirect(username)
    
@app.route("/<username>")
def get_userpage(username):
    return render_template("chat.html",logged_in_as=username, all_the_messages=messages)
    
# @app.route('rooms/add')
# def add_room():
#     roomname = request.form['roomname']
#     rooms[roomname] = []
#     return redirect(....)

@app.route('/<username>/new', methods=["POST"])
def add_message(username):
    
    text = request.form['message']
    
    words =text.split()
    words = ["*" * len(word) if word.lower() in banned_words else word for word in words]
        
    text="".join(map(str,words))
    
    message =  {
    "sender": username,
    "body": text
}

    messages.append(message)
    return redirect(username)

app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')), debug=True)

    if __name__ == '__main__':
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))