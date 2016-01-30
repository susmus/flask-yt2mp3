#!/usr/bin/python2
from flask import Flask, render_template, request, send_file, redirect
from subprocess import check_output, call
from os import chdir as cd
from re import match

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/download", methods=['POST'])
def download():
    url = request.form.get('url', type=str)
    if url == "":
        return redirect("/")

    out = check_output("youtube-dl -x --audio-format mp3 --prefer-avconv --audio-quality 0 --no-progress \"{}\"".format(url),
                       shell=True)

    for line in out.decode("utf-8").split("\n"):
        if "[avconv] Destination: " in line or "[ffmpeg] Destination: " in line:
            fname = line.split(": ")[1]
            break

        elif "Unfortunately, this video is not available in your country" in line:
            return render_template("unavailable.html")

    print("fname: " + str(fname))
    call("mv \"{0}\" mp3/\"{0}\"".format(fname), shell=True)
    return send_file("mp3/"+fname,
                     attachment_filename=fname,
                     as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0")

