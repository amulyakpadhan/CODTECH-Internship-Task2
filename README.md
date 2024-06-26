# Text-to-Image Conversion Application

Name: Amulya Kumar Padhan\
Company: CODTECH IT SOLUTIONS\
Domain: Machine learning\
Duration: June 1st to June 30th

## Overview
This project aims to develop a text-to-image generation application that transforms textual descriptions into visual representations using generative models. The application leverages the Diffusers library from HuggingFace to utilize advanced techniques in the field of machine learning for creating images from text.

## Features
- Input textual descriptions for image generation.
- Utilizes the Stable Diffusion model from HuggingFace's Diffusers library.
- Downloadable images in standard formats.
- Automatic cleanup of old generated images.

## Technologies Used
- Python 3.x
- PyTorch (for deep learning and generative models)
- HuggingFace Diffusers library (for Stable Diffusion model)
- Django 3.x or 4.x (web framework)
- HTML/CSS (Bootstrap for styling)
- JavaScript (jQuery)
- Git (for version control)
- Virtual environment tool like `venv` or `virtualenv` (recommended)

## Setup and Installation
Follow these steps to set up and run the project locally:

### Step 1: Clone the Repository
```bash
git clone https://github.com/amulyakpadhan/CODTECH-Internship-Task2.git
cd CODTECH-Internship-Task2
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# For Windows, use: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt  # Install the required packages
```

### Step 4: Configure Django Settings
Ensure your Django settings are configured properly:

- Set ALLOWED_HOSTS to include your local development domain.
- Configure DATABASES to use a suitable database (e.g., SQLite for development).
- Ensure MEDIA_ROOT and STATIC_ROOT are properly set to handle media files and static files.

### Step 5: Run Migrations
```bash
python manage.py migrate  # Apply database migrations
```

### Step 6: Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser  # Create an admin account
```
### Step 7: Start the Django Server
```bash
python manage.py runserver  # Start the Django development server
```
Now, you can access the project by navigating to http://127.0.0.1:8000/ in your web browser.

## Usage
- Open the application in your browser.
- Enter the textual description for the image you want to generate.
- Click the "Generate Image" button.
- The generated image will be displayed and available for download.


## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or fix.
- Make your changes and commit them with descriptive commit messages.
- Push to your fork and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
- Django: The web framework used in this project.
- Diffusers Library: HuggingFace library used for text-to-image generation.
- TensorFlow/PyTorch: Deep learning frameworks utilized for model training.

## 🚀 About Me
I'm Amulya Kumar Padhan, a computer science student specializing in artificial intelligence and web development. This project is a demonstration of my skills and expertise in building web-based applications that incorporate advanced technologies like machine learning, deep learning, web development etc.
