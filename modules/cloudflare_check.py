import os
import platform
import urllib.request
import stat

# === Terminal Colors ===
GREEN = '\033[0;32m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
RESET = '\033[0m'

# === Download Function ===
def download(url, output_name):
    try:
        print(f"{CYAN}[*] Downloading: {url}{RESET}")
        urllib.request.urlretrieve(url, output_name)
        os.chmod(output_name, os.stat(output_name).st_mode | stat.S_IEXEC)
        print(f"{GREEN}[+]{CYAN} Downloaded {output_name} and made it executable{RESET}")
    except Exception as e:
        print(f"{WHITE}[!] Failed to download: {e}{RESET}")

# === Main Logic ===
paths_to_check = ["cloudflared", "../cloudflared"]

cloudflared_exists = any(os.path.exists(path) for path in paths_to_check)

if cloudflared_exists:
    print("")
else:
    print(f"\n{GREEN}[{WHITE}+{GREEN}]{CYAN} Installing Cloudflared...{WHITE}")
    arch = platform.machine().lower()

    if "arm" in arch or "android" in arch:
        download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", "cloudflared")
        print("Run Script Again")
        exit()
    elif "aarch64" in arch:
        download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", "cloudflared")
        print("Run Script Again")
        exit()
    elif "x86_64" in arch:
        download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", "cloudflared")
        print("Run Script Again")
        exit()
    else:
        download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", "cloudflared")
        print("Run Script Again")
        exit()
