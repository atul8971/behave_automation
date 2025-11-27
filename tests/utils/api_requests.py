import requests


def simple_get(url, params=None, headers=None):
    """
    Simple GET request

    Args:
        url: Full URL for the request
        params: Query parameters (optional)
        headers: Request headers (optional)

    Returns:
        requests.Response object
    """
    response = requests.get(url, params=params, headers=headers)
    return response
