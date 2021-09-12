if not exist mctest-script/paper-1.17.1.jar (
    python mctest-script/download.py -v 1.17.1 -d
)
java -jar mctest-script/paper-1.17.1.jar nogui