gradlew build build

if exist mctest-script/paper-1.17.1.jar (
    java -jar mctest-script/paper-1.17.1.jar nogui
) else (
    python download.py -v 1.17.1 -d
)