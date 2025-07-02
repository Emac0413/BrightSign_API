import base64

print("🔥 utils.py LOADED")

def encode_image_to_base64(path: str) -> str:
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
