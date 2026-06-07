from flask import Blueprint, request
from store import upsert_client

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