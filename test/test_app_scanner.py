#!/usr/bin/env python3
"""
Test script for verifying the app-scanner package functionality.
"""

import sys
import os

# Add the project root directory to the path to import the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app_scanner import get_installed_apps

def main():
    print("Testing app-scanner package...")
    print(f"Current OS: {sys.platform}")

    try:
        apps = get_installed_apps()
        print(f"Found applications: {len(apps)}")

        if apps:
            for i, app in enumerate(apps):
                print(f"{i+1}. {app.get('name', 'Unknown')} - {app.get('appid', app.get('path', 'N/A'))}")
        else:
            print("No applications found.")

    except Exception as e:
        print(f"Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()