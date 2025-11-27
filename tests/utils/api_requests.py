import requests
from typing import Optional, Dict, Any


def simple_get(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 30
) -> requests.Response:
    """
    Simple GET request wrapper

    Args:
        url (str): Full URL for the request
        params (dict, optional): Query parameters to append to URL
        headers (dict, optional): HTTP headers to include in request
        timeout (int, optional): Request timeout in seconds (default: 30)

    Returns:
        requests.Response: Response object containing status code, headers, and body

    Raises:
        TimeoutError: If request exceeds timeout duration
        RuntimeError: If request fails due to network or connection issues
        requests.exceptions.HTTPError: If response status code indicates an error (4xx, 5xx)

    Example:
        >>> response = simple_get('https://api.example.com/data')
        >>> print(response.status_code)
        200
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        return response
    except requests.exceptions.Timeout:
        raise TimeoutError(f"Request to {url} timed out after {timeout} seconds")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {str(e)}") from e
