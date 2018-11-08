import os
import zipfile
import tempfile

def unpack():
    files = []
    for i in range(1, 5):
        files.append("app/static/data-" + str(i) + ".zip.part")

    with tempfile.TemporaryFile() as temp:
        for f in files:
            with open(f) as infile:
                temp.write(infile.read())
    
        zipped = zipfile.ZipFile(temp)
        zipped.extractall("app/static")
        zipped.close()

if __name__ == "__main__":
    if not os.path.isdir("app/static/data"):
        unpack()

    from app import app, socketio
    socketio.run(app, host="0.0.0.0", port=5000)
