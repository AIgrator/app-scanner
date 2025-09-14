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

## Return Values

The `get_installed_apps()` function returns a list of dictionaries, where each dictionary represents an installed application. The structure varies slightly by platform:

### Common Keys
- **`name`** (str): The display name of the application.

### Windows
- **`appid`** (str): Application ID used for launching (e.g., from Start Menu).

### macOS
- **`path`** (str): Full path to the .app bundle.
- **`bundle_id`** (str, optional): CFBundleIdentifier from Info.plist.
- **`version`** (str, optional): CFBundleShortVersionString or CFBundleVersion.
- **`executable`** (str, optional): CFBundleExecutable.
- **`icon`** (str, optional): Path to the .icns icon file if found.
- **`source`** (str): 'spotlight' or 'scan' (how it was discovered).

### Linux
- **`path`** (str): Path to the executable or .desktop file.
- **`package`** (str, optional): Package identifier (e.g., 'snap:firefox' or 'flatpak:org.mozilla.firefox').
- **`icon`** (str, optional): Path to the icon file.
- **`categories`** (str, optional): Application categories from .desktop file.
- **`description`** (str, optional): Description or comment from .desktop file.
- **`wm_class`** (str, optional): Window manager class.
- **`desktop_id`** (str, optional): Desktop file ID.
- **`variant`** (bool, optional): True if it's a specialized launcher variant.

## How it Works

- **Windows:** Uses PowerShell commands (`Get-StartApps` or `Get-AppxPackage`) to find installed applications from the Start Menu and returns app IDs for launching.
- **macOS:** Uses `mdfind` (Spotlight) to locate all `.app` bundles and reads their Info.plist for metadata.
- **Linux:** Scans for `.desktop` files in standard application directories including `/usr/share/applications`, `~/.local/share/applications`, and additional paths for Snap, Flatpak, AppImage, and other package managers.
