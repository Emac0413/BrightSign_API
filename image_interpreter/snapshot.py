import base64
import requests
from typing import Optional

print("🔥 snapshot.py LOADED")

def get_brightsign_snapshot(ip_address: str, save_path: str) -> Optional[str]:
    url = f"http://{ip_address}/api/v1/snapshot/"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "width": 640,
        "height": 480
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        image_data_url = result['data']['result']['remoteSnapshotThumbnail']

        if image_data_url.startswith("data:image/"):
            base64_str = image_data_url.split(",")[1]
        else:
            raise ValueError("Unexpected image format in response")

        with open(save_path, "wb") as f:
            f.write(base64.b64decode(base64_str))

        print(f"Snapshot saved to: {save_path}")
        return save_path

    except Exception as e:
        print(f"Error capturing snapshot: {e}")
        return None
