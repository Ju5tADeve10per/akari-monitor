from flask import Blueprint, request
from store import upsert_client, is_alive, get_clients

# Define a Blueprint to group related routes
bp = Blueprint("routes", __name__)

# Register POST /signal endpoint and map it to handle_signal
@bp.route("/signal", methods=["POST"])
def handle_signal() -> tuple[dict, int]:
    """
    Receive client signal and update its state.
    
    Returns:
        tuple[dict, int]: JSON response and HTTP status code
    """
    client_data = request.json
    if client_data is None:
        return {"error": "request body must be JSON"}, 400
    client_id = client_data.get("client_id")
    timestamp = client_data.get("timestamp")
    if client_id is None or timestamp is None:
        return {"error": "missing data"}, 400
    upsert_client(client_id, timestamp)
    return {"success": "ok"}, 200

# Register GET /clients endpoint and map it to handle_request
@bp.route("/clients", methods=["GET"])
def list_clients() -> tuple[dict[str, dict[str, float | int | bool]], int]:
    """
    Return all clients with their alive status.

    This endpoint is used by the management UI to fetch current client states.

    Returns:
        tuple[dict[str, dict[str, float | int | bool]], int]: 
            Mapping of client_id to client data (including "response" field)
            with HTTP 200 status code.
    """
    return get_clients_status(), 200
    
def get_clients_status() -> dict[str, dict[str, float | int | bool]]:
    """
    Get all clients and attach their alive status.
    
    Returns:
        dict[str, dict[str, float | int | bool]]:
            Clients data with additional "response" field indicating alive status
    """
    clients_data = get_clients()
    clients_formatted_data = {}

    for client_id in clients_data:
        clients_formatted_data[client_id] = clients_data[client_id].copy() # shallow copy is enough because the data structure is single-layer
        clients_formatted_data[client_id]["response"] = is_alive(client_id)

    return clients_formatted_data