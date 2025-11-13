# Make sure venv is installed
sudo apt install python3-venv python3-full

# Create a virtual environment in your project folder
python3 -m venv venv

# Activate it
source venv/bin/activate

# Now install Flask inside the venv
pip install Flask
