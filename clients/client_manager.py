from make_post_request import make_post_request
from send_signal import send_post_request

# current_clients = [
#   "client1",
#   "client2"
#]
current_clients = []

def create_client():
    # input client info -> id
    client_id = input()
    get_current_clients().append(client_id)
    data = make_post_request(client_id)
    url = "http://localhost:8000/signal" # これはグローバルな定数で固定すると良いかも。
    result = send_post_request(url, data)
    return result

def get_current_clients():
    return current_clients

def show_client_list():
    print(current_clients)