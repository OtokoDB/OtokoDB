import requests
import zippyshare_downloader
f = open("asmr-url.txt", "r+")
err = open("asmr-error.log", "w+")
while True:
    url_orig = f.readline().strip("\n")
    if url_orig == "":
        break
    else:
        url_zippy = requests.get(url_orig).url
    if "japaneseasmr" in url_zippy:
        print("Download Failed: No source available: " + url_orig)
        err.write(url_orig + '\n')
        continue
    try:
        zippyshare_downloader.download(url_zippy)
    except BaseException:
        print("Download Failed: File deleted or banned: " + url_orig)
        err.write(url_orig + '\n')
    else:
        print("Download successfully: " + url_orig)
f.close()
err.close()
print("Download ended.")
