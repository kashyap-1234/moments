import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()
# Load Azure credentials from environment variables
AZURE_VISION_API_KEY = os.getenv("API_KEY")
AZURE_VISION_ENDPOINT = os.getenv("API_ENDPOINT")

# Initialize Azure Image Analysis Client
client = ImageAnalysisClient(endpoint=AZURE_VISION_ENDPOINT, credential=AzureKeyCredential(AZURE_VISION_API_KEY))

def analyze_image(image_path):
    """Analyze an image using Azure AI Vision and extract alt text & object tags."""
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        # Call Azure Image Analysis API
        result = client.analyze(image_data=image_data, visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS])

        # Extract caption (alt text)
        alt_text = result.caption.text if result.caption else "No description available"

        # Extract tags (objects detected)
        tags = ", ".join(tag.name for tag in result.tags.list) if result.tags else ""
        print(alt_text, tags)
        return alt_text, tags
    except Exception as e:
        print(f"Azure Vision API Error: {e}")
        return "No description available", ""
