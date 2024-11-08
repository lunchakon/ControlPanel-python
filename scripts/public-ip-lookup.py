import requests

def get_public_ip():
    """Gets the public IP address using a public API.

    Returns:
        The public IP address as a string, or None if an error occurs.
    """

    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        return response.json()["ip"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print(f"Your public IP address is: {public_ip} ")
        response2 = requests.get("https://ifconfig.me").text
        print(" IP ",response2)
    else:
        print("Failed to retrieve public IP address.")