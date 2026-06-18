# current_clients = [
#   "client1",
#   "client2"
#]
current_clients = []

def create_client():
    # input client info -> id
    client_id = input(): # must be str
    current_clients.add(client_id)
    data = make_post_request(client_id)
    result = send_post_request(client_id, data)
    return result

def show_client_list():
    print(current_clients)