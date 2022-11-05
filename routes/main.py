from app import app
from models.models import Plant
from flask import render_template


@app.route("/")
def main():
    plants = Plant.get_data()
    return render_template("index.html", plants=plants)
