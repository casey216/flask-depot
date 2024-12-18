import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from app import create_app

# Get the configuration name from environment variable
config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)



if __name__ == '__main__':
    app.run()
