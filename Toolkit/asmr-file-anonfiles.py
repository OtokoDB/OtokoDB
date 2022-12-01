import requests
import re
f = open("asmr-url.txt", "r+")
err = open("error.log", "w+")
succ = open("success.log", "w+")
while True:
    url_orig = f.readline().strip('\n')
    if url_orig == "":
        break
    else:
        url_anon = requests.get(url_orig).url
    if ("japaneseasmr" in url_anon):
        print("Download Failed: No source available: " + url_orig)
        err.write(url_orig + '\n')
    else:
        anon_id = re.findall(r"com/(.+?)/", url_anon)
        url_info = "https://api.anonfiles.com/v2/file/" + anon_id[0] + "/info"
        info_json = requests.get(url_info).json()
        status = info_json["status"]
        if status == False:
            print("Download Failed: Status check failed: " + url_orig)
            err.write(url_orig + '\n')
        else:
            print("Extract successfully: " + url_orig)
            succ.write(url_orig + '\n')
f.close()
err.close()
succ.close()
print("Download ended.")
