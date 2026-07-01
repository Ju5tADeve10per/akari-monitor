from requests import post, Response

def send_post_request(url: str, data: dict) -> Response:
    """
    Send alive signal to the server

    Args:
        url (str): The url of the server
        data (dict): request body containing client_id and timestamp
    
    Returns:
        Response: the response object from the server
    """
    return post(url, json=data)

def display_response_status(res: Response) -> None:
    """
    Show the result of the server response

    Args:
        res (Response): the response object returned from the server
    
    Returns:
        None
    """
    print(f"{res.status_code} {res.text}")