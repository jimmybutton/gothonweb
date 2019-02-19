from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import game

app = Flask(__name__)

@app.route("/")
def index():
    # this is used to set up the session with starting values
    session['room_name'] = game.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = game.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is this here? do you need it?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = game.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = game.name_room(room)
            else:
                session['room_name'] = game.name_room(next_room)

        return redirect(url_for("game"))

app.secret_key = 'K_D*(YSDH:Q£"?KTasy56IADS(RF%^&*(Q!I24357uijgGHK")'

if __name__ == "__main__":
    app.run()
