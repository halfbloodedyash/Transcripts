from flask import Flask, request, jsonify, render_template
from youtube_tools import YouTubeTools

app = Flask(__name__)
yt_tools = YouTubeTools()

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        action = request.form.get("action")

        if not url:
            result = "Please provide a valid YouTube URL."
        else:
            if action == "captions":
                result = yt_tools.get_youtube_video_captions(url)
            elif action == "metadata":
                result = yt_tools.get_youtube_video_data(url)
            elif action == "timestamps":
                result = yt_tools.get_video_timestamps(url)
            else:
                result = "Unknown action selected."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
