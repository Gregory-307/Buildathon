#!/usr/bin/env python
"""
Set the OpenAI API key in the .env file.
This script takes a key from command line arguments or from the OPENAI_API_KEY environment variable 
and sets it in the .env file for use by the application.
"""

import os
import sys
import re
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def is_valid_openai_key(key):
    """Basic validation for OpenAI API key format."""
    # Current OpenAI keys start with "sk-"
    pattern = r'^sk-[A-Za-z0-9]{32,}$'
    return bool(re.match(pattern, key))

def main():
    parser = argparse.ArgumentParser(description='Set the OpenAI API key in the .env file.')
    parser.add_argument('--key', help='The OpenAI API key to set. If not provided, will use OPENAI_API_KEY environment variable.')
    parser.add_argument('--env-file', default='.env', help='Path to the .env file (default: .env)')
    args = parser.parse_args()
    
    # Get the API key
    api_key = args.key or os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        logger.error("No API key provided. Please provide it via --key argument or set the OPENAI_API_KEY environment variable.")
        return 1
    
    # Basic validation
    if not is_valid_openai_key(api_key):
        logger.warning("The provided API key doesn't match the expected format for OpenAI API keys.")
        confirm = input("The key doesn't look like a valid OpenAI API key. Continue anyway? (y/n): ")
        if confirm.lower() != 'y':
            logger.info("Operation cancelled by user.")
            return 1
    
    # Create or update the .env file
    env_file = args.env_file
    env_content = {}
    
    # Read existing .env file if it exists
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_content[key] = value
    
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
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 