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
    # clientsを取得
    clients_data = get_clients()
    # clientsをベースにループでis_aliveを呼び、返り値を返す。（管理UI上での正常に信号が来てるのか結果）
    for client_id in clients_data:
        # TODO: ループ内でresponseを新たな項目に加えたclients_dataをベースにした新たなデータ構造を作って返す処理をする。
        # clientsにある各clientデータとis_aliveの呼び出し結果を一つのデータ構造にする。
        clients_data[client_id]["response"] = is_alive(client_id)
    # その新たなデータをreturnする。
    return clients_data