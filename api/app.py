from flask import Flask, make_response
import pandas as pd

app = Flask(__name__)

tipos = None


# One-time initialization
def load_data():
    global tipos
    try:
        # OBS: Filename hardcoded only for the test
        tipos = pd.read_csv("../dados/tipos.csv")
    except Exception as e:
        print(f"Error loading CSV: {e}")


with app.app_context():
    load_data()


@app.route("/tipo/<int:tipo_id>", methods=["GET"])
def get_type_by_id(tipo_id):
    data = tipos.loc[tipos["id"] == tipo_id]

    if data.empty:
        response = make_response("ID not found")
        response.status_code = 404
        return response

    tipo = data["nome"].values[0]

    response = make_response({"tipo": tipo})  # JSON format
    response.status_code = 200
    return response
