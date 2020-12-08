from flask import Flask, render_template, request
import sqlite3
app=Flask(__name__)

@app.route("/")
def leaderboard():
    con=sqlite3.connect("scoreboard.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    rows=cur.fetchall()
    if rows == []:
        cur.execute("SELECT * FROM 'leaders' ORDER BY score DESC;")
        rows=cur.fetchall()
    print(rows)
    return render_template("template.html",rows=rows)

@app.route("/search", methods=["POST"])
def search():
    payload=request.form["payload"]
    con=sqlite3.connect("scoreboard.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.executescript(payload) 
    return ('', 204)

    
if __name__ == '__main__':
    app.run(debug=True)
#payload=UPDATE leaders SET score = 969691337 where team = 'InfoSecIITR'
