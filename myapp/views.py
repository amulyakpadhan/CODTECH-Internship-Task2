import requests
import datetime
from io import BytesIO
from PIL import Image
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.conf import settings
from .forms import ImageGenerationForm
import os

def generate_image(prompt, aspect_ratio):
    url = settings.URL
    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio
    }
    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "image/png",
        "Authorization": settings.API_KEYS
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        return image
    except requests.exceptions.RequestException as e:
        print(f"Error generating image: {e}")
        return None

def index(request):
    if request.method == 'POST':
        form = ImageGenerationForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            aspect_ratio = form.cleaned_data['aspect_ratio']
            image = generate_image(prompt, aspect_ratio)
            
            if image:
                # Save the image to the media directory
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                image_name = f'generated_img_{timestamp}.png'
                image_path = os.path.join(settings.MEDIA_ROOT, image_name)
                image.save(image_path)
                return render(request, 'index.html', {'form': form, 'image_url': settings.MEDIA_URL + image_name, 'image_filename': image_name})
    else:
        form = ImageGenerationForm()
    
    return render(request, 'index.html', {'form': form})

def cleanup_old_audio_files():
    # Define the threshold for old audio files (e.g., files older than 7 days)
    threshold_date = datetime.datetime.now() - datetime.timedelta(days=7)

    # Iterate over the files in the media folder
    for filename in os.listdir(settings.MEDIA_ROOT):
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.isfile(file_path):
            # Get the creation time of the file
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            # Check if the file is older than the threshold date
            if creation_time < threshold_date:
                # Delete the file
                os.remove(file_path)

def schedule_audio_cleanup():
    # Schedule the cleanup task to run periodically (e.g., daily)
    cleanup_old_audio_files()

# Call the schedule_audio_cleanup function when this module is imported
schedule_audio_cleanup()

def about(request):
    return render(request, 'about.html')