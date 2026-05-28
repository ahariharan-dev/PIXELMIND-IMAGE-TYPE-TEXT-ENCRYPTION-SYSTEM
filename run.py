import os
import sys

# Get the absolute path of the project root
project_root = os.path.dirname(os.path.abspath(__file__))

# Add the project root and app directory to Python path
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'app'))

# Set the PYTHONPATH environment variable
os.environ['PYTHONPATH'] = project_root

# Load .env only in local development
if os.environ.get('RENDER') is None:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(project_root, '.env'))

# Now import the app
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
