# App Scanner

A cross-platform Python utility to find installed applications on Windows, macOS, and Linux.

This library provides a simple function, `get_installed_apps()`, that returns a list of installed applications on the host operating system.

## Features

- **Cross-Platform:** Works on Windows, macOS, and Linux.
- **Simple API:** A single function to get the list of apps.
- **Lightweight:** No external dependencies.

## Installation

```bash
pip install installed-apps-scanner
```

## Usage

```python
from app_scanner import get_installed_apps

apps = get_installed_apps()

for app in apps:
    name = app['name']
    # On Windows, 'appid' is used as identifier; on macOS/Linux, 'path' is used
    identifier = app.get('appid') or app.get('path', 'N/A')
    print(f"Name: {name}, Identifier: {identifier}")
```

## How it Works

- **Windows:** Uses PowerShell commands (`Get-StartApps` or `Get-AppxPackage`) to find installed applications from the Start Menu and returns app IDs for launching.
- **macOS:** Uses `mdfind` (Spotlight) to locate all `.app` bundles and reads their Info.plist for metadata.
- **Linux:** Scans for `.desktop` files in standard application directories including `/usr/share/applications`, `~/.local/share/applications`, and additional paths for Snap, Flatpak, AppImage, and other package managers.
