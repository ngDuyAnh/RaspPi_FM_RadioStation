from flask import Flask, render_template, request
import os
import subprocess
from pytube import YouTube

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        req = request.get_json()
        main(req[0]['value'])

    return render_template("index.html")


def main(url):
    # get current working directory
    cwd = os.getcwd()
    downloadDirectory = r"{}\music".format(cwd)

    # Get the youtube video object
    video_object = YouTube(url)

    # highest resolution audio (formatted as .mp4)
    audio = video_object.streams.get_audio_only()

    file = video_object.streams.filter(only_audio=True)
    audio.download(filename="file", output_path=downloadDirectory)

    # file names
    filename = "file"
    newfilename = "Converted_" + filename + ".wav"

    # run the ffmpeg cmd to convert to a specific .wav file
    cmd = "ffmpeg -i " + os.path.join(downloadDirectory,
                                      filename) + " -f wav -bitexact -acodec pcm_s16le -ar 22050 -ac 1 " + os.path.join(
        downloadDirectory, newfilename)
    subprocess.run(cmd.split())

    os.remove(os.path.join(downloadDirectory, filename))

if __name__ == '__main__':
    app.run()
