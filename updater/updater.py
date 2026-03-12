import requests

def check_for_updates(current_version="1.0.0"):
    """
    Checks GitHub Releases for a newer version.
    Returns (latest_version, download_url) if update available, else None.
    """
    repo = "infinityambients-tech/Raw_2_Jpg"
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get("tag_name", current_version)
            
            if latest_version != current_version:
                # Find the installer asset (looking for .exe or .dmg)
                assets = data.get("assets", [])
                download_url = None
                for asset in assets:
                    if asset["name"].endswith((".exe", ".dmg", ".zip")):
                        download_url = asset["browser_download_url"]
                        break
                return latest_version, download_url
    except Exception as e:
        print(f"Update check failed: {e}")
        
    return None
