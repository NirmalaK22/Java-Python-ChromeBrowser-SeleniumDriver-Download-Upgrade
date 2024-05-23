import subprocess
import urllib.request
import json
import psutil

def get_installed_chrome_version():
    try:
        output = subprocess.check_output(
            r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',
            shell=True
        ).decode()
        for line in output.splitlines():
            if "version" in line:
                return line.split()[-1]
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking the installed Chrome version: {e}")
    return None

def get_latest_chrome_version():
    try:
        url = "https://versionhistory.googleapis.com/v1/chrome/platforms/win/channels/stable/versions"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data and 'versions' in data and len(data['versions']) > 0:
                return data['versions'][0]['version']
    except Exception as e:
        print(f"An error occurred while fetching the latest Chrome version: {e}")
    return None

def download_latest_chrome_installer_windows():
    url = 'https://dl.google.com/chrome/install/latest/chrome_installer.exe'
    output_file = 'chrome_installer.exe'

    try:
        urllib.request.urlretrieve(url, output_file)
        print("Chrome installer downloaded successfully.")
        return output_file
    except Exception as e:
        print(f"An error occurred during download: {e}")
        return None

def install_chrome_windows(installer_path):
    try:
        subprocess.run([installer_path, "/silent", "/install"], check=True)
        print("Chrome has been installed/upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e}")

def kill_chrome_windows():
    try:
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], check=True)
        print("Chrome has been closed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while closing Chrome: {e}")

def kill_latest_chrome_browser(pid):
    try:
        print("closing latest browser method")
        process = psutil.Process(pid)
        process.kill()
        process.wait(3)
        print(f"Chrome with PID {pid} is closed")
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} does not exist.")
    except psutil.AccessDenied:
        print(f"Access denied to terminate process with PID {pid}.")
    except Exception as e:
        print(f"An error occurred while closing Chrome: {e}")


def list_chrome_windows():
    chrome_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in ('chrome', 'chrome.exe'):
                chrome_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return chrome_processes

def get_latest_chrome_pid():
    chrome_pids = []
    print("getting latest chrome")
    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            if proc.info['name'].lower() in ('chrome', 'chrome.exe'):
                chrome_pids.append((proc.info['pid'], proc.info['create_time']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if not chrome_pids:
        return None
    chrome_pids.sort(key=lambda x: x[1], reverse=True)
    return chrome_pids[0][0]

if __name__ == "__main__":
    installed_version = get_installed_chrome_version()
    latest_version = get_latest_chrome_version()

    if installed_version and latest_version:
        print(f"Installed Chrome version: {installed_version}")
        print(f"Latest Chrome version: {latest_version}")

        if installed_version != latest_version:
            print("An update is available. Downloading and installing the latest version...")
            installer = download_latest_chrome_installer_windows()
            if installer:
                install_chrome_windows(installer)
                latest_chrome_pid = get_latest_chrome_pid()
                kill_latest_browser = kill_latest_chrome_browser(latest_chrome_pid)
                print("latest chrome is upgraded")
        else:
            print("Chrome is already up-to-date.")
    else:
        print("Could not determine the installed or latest Chrome version.")
