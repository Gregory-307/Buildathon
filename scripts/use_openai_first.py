#!/usr/bin/env python
"""
Helper script to switch to the OpenAI-first implementation.
This script:
1. Checks if OpenAI is properly configured
2. Backs up the current app.py
3. Renames app_openai_first.py to app.py
"""

import os
import shutil
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def check_openai_config():
    """Check if OpenAI is properly configured."""
    load_dotenv()
    
    openai_key = os.environ.get('OPENAI_API_KEY')
    if not openai_key:
        logger.error("OpenAI API key not found in .env file")
        return False
    
    logger.info("OpenAI API key found in .env file")
    return True

def backup_current_app():
    """Backup the current app.py file."""
    if not os.path.exists('app.py'):
        logger.error("app.py not found. Nothing to backup.")
        return False
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"app_backup_{timestamp}.py"
    
    try:
        shutil.copy2('app.py', backup_filename)
        logger.info(f"Current app.py backed up to {backup_filename}")
        return True
    except Exception as e:
        logger.error(f"Failed to backup app.py: {str(e)}")
        return False

def switch_to_openai_first():
    """Switch to the OpenAI-first implementation."""
    if not os.path.exists('app_openai_first.py'):
        logger.error("app_openai_first.py not found. Cannot switch.")
        return False
    
    try:
        # Replace app.py with app_openai_first.py
        shutil.copy2('app_openai_first.py', 'app.py')
        logger.info("Successfully switched to OpenAI-first implementation")
        return True
    except Exception as e:
        logger.error(f"Failed to switch to OpenAI-first implementation: {str(e)}")
        return False

def main():
    """Main entry point."""
    logger.info("Starting switch to OpenAI-first implementation")
    
    # Check if OpenAI is configured
    if not check_openai_config():
        logger.error("Please set the OPENAI_API_KEY in your .env file")
        return 1
    
    # Confirm with user
    confirm = input("This will replace your current app.py with the OpenAI-first implementation. Continue? (y/n): ")
    if confirm.lower() != 'y':
        logger.info("Operation cancelled by user")
        return 0
    
    # Backup current app
    if not backup_current_app():
        logger.error("Failed to backup current app.py. Operation aborted.")
        return 1
    
    # Switch to OpenAI-first
    if not switch_to_openai_first():
        logger.error("Failed to switch to OpenAI-first implementation")
        return 1
    
    logger.info("=" * 50)
    logger.info("Successfully switched to OpenAI-first implementation!")
    logger.info("You can now run the app with: python app.py")
    logger.info("=" * 50)
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 