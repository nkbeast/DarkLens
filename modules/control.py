from colorama import Fore,Back,Style
import subprocess,json,time,hashlib,os

def kill_php_proc():
    with open("darkLens-web/Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
        pid = data["pid"]

    try:
        for i in pid:
            subprocess.getoutput(f"kill -9 {i}")
            os.system("rm .cld.log")
            os.system("killall cloudflared")


        
        else:
            pid.clear()
            data["pid"] = []
            with open("darkLens-web/Settings.json", "w") as jsonFile:
                json.dump(data, jsonFile)

    except:
        pass



def md5_hash():
    str2hash = time.strftime("%Y-%m-%d-%H:%M", time.gmtime())
    result = hashlib.md5(str2hash.encode())
    return result



def run_php_server(port):
    with open(f"darkLens-web/log/php-{md5_hash().hexdigest()}.log","w") as php_log:
        proc_info = subprocess.Popen(("php","-S",f"localhost:{port}","-t","darkLens-web"),stderr=php_log,stdout=php_log).pid


    with open("darkLens-web/Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data["pid"].append(proc_info)


    with open("darkLens-web/Settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    print(Fore.RED+" [+] "+Fore.GREEN+"Web Panel Link :  "+Fore.WHITE+f"http://localhost:{port}")
    os.system('./cloudflared tunnel --url "localhost:2525" --logfile .cld.log > /dev/null 2>&1 &')
    os.system("sleep 10")
    command = "cat .cld.log | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'"
    cloudf = subprocess.run(command, shell=True, text=True, capture_output=True)
    if cloudf.returncode == 0:
    	output_lines = cloudf.stdout.splitlines()  # Split into lines
    	cleaned_output = [line.strip() for line in output_lines if line.strip()]  # Remove empty or whitespace-only lines
    	for line in cleaned_output:
    		#print(Fore.RED+"\n [+] "+Fore.GREEN+"Web Panel Link 2 : "+Fore.LIGHTCYAN_EX+, (line)+Style.RESET_ALL)
    		print(Fore.RED+"\n [+] "+Fore.GREEN+"Web Panel Link 2 :"+Fore.LIGHTCYAN_EX+" ", line)
    		os.system("echo ''")
    else:
    	print(f"Error: {cloudf.stderr}")

