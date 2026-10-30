import requests

# Your Ngrok URL
BASE_URL = "https://flavoring-dayroom-mute.ngrok-free.dev"

# Required header to bypass Ngrok's HTML warning page
headers = {
    "ngrok-skip-browser-warning": "true"
}

# 1. Test Root Endpoint
try:
    response = requests.get(f"{BASE_URL}/", headers=headers)
    print("Root response:", response.json())
except Exception as e:
    print("Root error:", e)

# 2. Test UPI Status Endpoint
try:
    response_upi = requests.get(f"{BASE_URL}/upi-status", headers=headers)
    print("UPI Status response:", response_upi.json())
except Exception as e:
    print("UPI Status error:", e)