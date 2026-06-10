from flask import Blueprint, request
from store import upsert_client, is_alive, get_clients

bp = Blueprint("routes", __name__)

@bp.route("/signal", methods=["POST"])
def handle_signal():
    client_data = request.json
    if client_data is None:
        return {"error": "request body must be JSON"}, 400
    client_id = client_data.get("client_id")
    timestamp = client_data.get("timestamp")
    if client_id is None or timestamp is None:
        return {"error": "missing data"}, 400
    upsert_client(client_id, timestamp)
    return {"success": "ok"}, 200

def get_clients_status():
    clients_data = get_clients()
    clients_formatted_data = {}

    for client_id in clients_data:
        clients_formatted_data[client_id] = clients_data[client_id].copy() #前提となる定義したデータ構造が、単階層なのでこのコピーで大丈夫
        clients_formatted_data[client_id]["response"] = is_alive(client_id)

    return clients_formatted_data