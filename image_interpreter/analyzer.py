from openai import OpenAI
from image_interpreter.utils import encode_image_to_base64
from image_interpreter.config import OPENAI_API_KEY

print("🔥 analyzer.py LOADED")

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_images(image1_path: str, image2_path: str) -> None:
    base64_img1 = encode_image_to_base64(image1_path)
    base64_img2 = encode_image_to_base64(image2_path)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Compare these two images in detail. If they have similar text(such as ip info) and colored backgrounds "
                            "respond only with: 'Error has occurred'. If they are different, give a short two-sentence description "
                            "of the differences, then end the response with: 'The player is working correctly'."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_img1}"}
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_img2}"}
                    }
                ]
            }
        ],
        max_tokens=1000
    )

    output = response.choices[0].message.content.strip()
    print("\nGPT-4 Analysis:")
    print("-" * 50)
    print(output)
