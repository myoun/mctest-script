
import urllib3
import argparse
import certifi
from datetime import datetime
import shutil


def download(version):
    url = f"https://papermc.io/api/v1/paper/{version}/latest/download"
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    r = http.request('GET', url, preload_content=False)
    file_size = int(r.headers["Content-Length"])
    print(f"Downloading : paper-{version}.jar Bytes : {file_size}")

    file_size_dl = 0
    block_sz = 8192
    with open(f"paper-{version}.jar", "wb") as f:
        print(f"Downloading paper-{version}.jar")
        started = datetime.now()
        while True:
            buffer = r.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = f"{int(file_size_dl * 100. // file_size)}"
            print(f"Downloaded {status}%")
        ended = datetime.now()
        delta = ended-started
        print(f"Successfully downloaded in {delta.seconds} seconds.")


parser = argparse.ArgumentParser(description="Minecraft PaperMC Test Script")
parser.add_argument("-v", "--version", action="store", dest="version", type=str)
parser.add_argument("-d", "--download", action="store_true")
args = parser.parse_args()

version = args.version
if args.download:
    if version != "":
        download(version)

shutil.move("paper-{}.jar".format(version),"./mctest-script/")
with open("mctest-script/eula.txt", "w") as f:
    print("Writing Eula File...")
    f.write("eula=true")
    print("Writing Finished")