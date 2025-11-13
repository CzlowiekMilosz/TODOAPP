import requests

def test_server():
    try:
        # Change URL to host port mapped to container
        r = requests.get("http://127.0.0.1:5002/")
        print("Status code:", r.status_code)
        print("Response:", r.json())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_server()
