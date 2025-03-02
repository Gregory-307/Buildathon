#!/usr/bin/env python
"""
Set the OpenAI API key using the one provided in the conversation.
Saves it to .env file for the application to use.
"""

import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def set_key_in_env_file(api_key, env_file='.env'):
    """Set the provided API key in the .env file."""
    # Create or update the .env file
    env_content = {}
    
    # Read existing .env file if it exists
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        key, value = line.split('=', 1)
                        env_content[key] = value
                    except ValueError:
                        # Skip lines that don't have the key=value format
                        pass
    
    # Update or add the OpenAI API key
    env_content['OPENAI_API_KEY'] = api_key
    
    # Set USE_MOCK_DATA to True for testing purposes
    env_content['USE_MOCK_DATA'] = 'True'
    
    # Write the updated .env file
    with open(env_file, 'w') as f:
        for key, value in env_content.items():
            f.write(f"{key}={value}\n")
    
    logger.info(f"OpenAI API key has been set in {env_file}")
    logger.info("Mock data has been enabled for testing")

def main():
    # The API key from the conversation (DO NOT COMMIT THIS TO VERSION CONTROL)
    api_key = "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"
    
    if not api_key or not api_key.startswith("sk-"):
        logger.error("The API key doesn't look like a valid OpenAI API key.")
        return 1
    
    # Set the key in the .env file
    set_key_in_env_file(api_key)
    
    # Also set it in the environment for the current session
    os.environ['OPENAI_API_KEY'] = api_key
    
    logger.info("API key has been set successfully!")
    logger.info("You can now run the application with OpenAI support.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 