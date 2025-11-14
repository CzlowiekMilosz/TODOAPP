import requests

def test_server():
    try:
        # Connect to the server on port 5000 (app exposes 5000)
        r = requests.get("http://127.0.0.1:5000/")
        print("Status code:", r.status_code)
        print("Response:", r.json())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_server()
