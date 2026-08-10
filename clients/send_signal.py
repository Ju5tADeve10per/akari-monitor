from requests import post, Response
from requests.exceptions import RequestException

def send_post_request(url: str, data: dict) -> Response | None:
    """
    Send alive signal to the server

    Args:
        url (str): The url of the server
        data (dict): request body containing client_id and timestamp
    
    Returns:
        Response: the response object from the server
    """
    try:
        res = post(url, json=data)
        return res
    except RequestException:
        print("Failed to connect to server")
        return None


def display_response_status(res: Response) -> None:
    """
    Show the result of the server response

    Args:
        res (Response): the response object returned from the server
    """
    print("\n\033[033mRESPONSE: ")
    print(f"{res.status_code} {res.text}\033[0m")