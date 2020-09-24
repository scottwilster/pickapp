from flask import Flask, jsonify, render_template

from utils import sql_to_df

app = Flask(__name__)


@app.route("/")
def hello():
    tbl_df = sql_to_df("picks_bet")
    return render_template("index.html", latest_team_list=tbl_df.to_dict("index"))


@app.route("/_pick_data")
def call_pick_data():
    return jsonify(sql_to_df("picks_bet").to_list())


if __name__ == "__main__":
    app.run(debug=True)