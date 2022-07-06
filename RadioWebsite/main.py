import signal

from flask import Flask, render_template, request
from flask_cors import CORS
import os
import subprocess
from pytube import YouTube

audioProcess = None # The radio audio process

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        req = request.get_json()
        print(type(req))
        print(req)
        print(req[0])
        main(req[0]['value'])

    return render_template("index.html")


def main(url):
    # Global variable
    global audioProcess

    # get current working directory
    print("Music folder")
    cwd = os.getcwd()
    downloadDirectory = r"{}/music".format(cwd)

    # Get the youtube video object
    video_object = YouTube(url)

    # highest resolution audio (formatted as .mp4)
    audio = video_object.streams.get_audio_only()

    file = video_object.streams.filter(only_audio=True)
    audio.download(filename="file", output_path=downloadDirectory)
    print("Download music in MP4")

    # file names
    filename = "file"
    newfilename = "Converted" + ".wav"

    # run the ffmpeg cmd to convert to a specific .wav file
    cmd = "ffmpeg -y -i " + os.path.join(downloadDirectory,
                                      filename) + " -f wav -bitexact -acodec pcm_s16le -ar 22050 -ac 1 " + os.path.join(
        downloadDirectory, newfilename)
    subprocess.run(cmd.split())
    print("Convert.wav")

    # Turn off the current transition
    if audioProcess is not None:
        audioProcess.kill()
        audioProcess = None

    # Playing the converted file
    audioCommand = "sudo ./fm_transmitter -r -f 108.0 " + downloadDirectory + "/" + newfilename
    audioProcess = subprocess.Popen(audioCommand)

    # Remove the MP4 file
    os.remove(os.path.join(downloadDirectory, filename))

if __name__ == '__main__':
    # Run the application
    app.run()
