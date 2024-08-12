from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion():
    text_to_analyze = request.args["textToAnalyze"]

    res = emotion_detector(text_to_analyze)

    if res["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return "For the given statement, the system response is" \
    f" 'anger': {res['anger']}," \
    f" 'disgust': {res['disgust']}," \
    f" 'fear': {res['fear']}," \
    f" 'joy': {res['joy']} and" \
    f" 'sadness': {res['sadness']}." \
    f" The dominant emotion is {res['dominant_emotion']}."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
