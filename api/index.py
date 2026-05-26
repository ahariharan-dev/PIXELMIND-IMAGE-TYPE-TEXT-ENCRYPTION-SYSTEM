import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(PROJECT_ROOT, 'app')

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, APP_DIR)  # This lets app.py find image_operations, database, etc.

from app.app import create_app

app = create_app()
