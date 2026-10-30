# qr_inspector.py
import re
from urllib.parse import parse_qs, urlparse
from pyzbar.pyzbar import decode
from PIL import Image

def inspect_qr_and_links(image_path_or_bytes):
    # 1. Decode QR Code
    img = Image.open(image_path_or_bytes)
    decoded_objects = decode(img)
    
    if not decoded_objects:
        return {"error": "No QR code detected"}
    
    qr_data = decoded_objects[0].data.decode('utf-8')
    
    parsed_info = {
        "raw_payload": qr_data,
        "payload_type": "UNKNOWN",
        "url_warnings": [],
        "extracted_params": {}
    }

    # 2. Parse payload type
    if qr_data.startswith("upi://pay"):
        parsed_info["payload_type"] = "UPI_INTENT"
        parsed_url = urlparse(qr_data)
        params = parse_qs(parsed_url.query)
        # UPI Parameters: pa (payee VPA), pn (payee name), am (amount)
        parsed_info["extracted_params"] = {k: v[0] for k, v in params.items()}
        
    elif qr_data.startswith("http://") or qr_data.startswith("https://"):
        parsed_info["payload_type"] = "URL"
        
        # Heuristic suspicious URL checks
        domain = urlparse(qr_data).netloc
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain):
            parsed_info["url_warnings"].append("IP address used instead of domain name")
        if any(keyword in qr_data.lower() for keyword in ["kyc", "reward", "cashback", "support-gpay", "paytm-login"]):
            parsed_info["url_warnings"].append("Phishing keywords detected in URL")
        if len(qr_data) > 75:
            parsed_info["url_warnings"].append("Suspiciously long URL path")

    return parsed_info