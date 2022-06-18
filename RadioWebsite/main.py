from flask import Flask, render_template, request
import os
import subprocess
from pytube import YouTube

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    print('WEEEE')

    if request.method == 'POST':
        print("WEEEEWEWEW" + request.form("form_input"))

    return render_template("index.html")


# @app.route('/', methods=['POST'])
# def download_Convert_Video():
#     print("WEEEEWEWEW"+request.form("form_input"))
#     return True


def main():
    # get current working directory
    cwd = os.getcwd()
    downloadDirectory = r"{}\music".format(cwd)

    video_object = YouTube('https://www.youtube.com/watch?v=NtzDjNhPZgU&ab_channel=ClearCode')

    # highest resolution audio (formatted as .mp4)
    audio = video_object.streams.get_audio_only()

    file = video_object.streams.filter(only_audio=True)
    audio.download(filename=audio.default_filename.replace(" ", "_"), output_path=downloadDirectory)

    # file names
    filename = audio.default_filename.replace(" ", "_")
    newfilename = "Converted_" + filename.split(".")[0] + ".wav"

    # run the ffmpeg cmd to convert to a specific .wav file
    cmd = "ffmpeg -i " + os.path.join(downloadDirectory,
                                      filename) + " -f wav -bitexact -acodec pcm_s16le -ar 22050 -ac 1 " + os.path.join(
        downloadDirectory, newfilename)
    subprocess.run(cmd.split())


if __name__ == '__main__':
    app.run(debug=True)
    # main()
