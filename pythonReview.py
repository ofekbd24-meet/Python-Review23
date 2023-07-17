# this disctionary has the functionality of a class
# instead you can write it as a class easily
import speech_recognition as sr

def create_youtube_video(title: str, description: str, hashtags: list) -> dict:
    video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": [],
        "hashtag": hashtags[0:5]
    }
    return video

def like(youtube_video: dict) -> dict:
    youtube_video["likes"] += 1
    return youtube_video

def dislike(youtube_video: dict) -> dict:
    youtube_video["dislikes"] += 1
    return youtube_video

def add_comment(youtube_video: dict, username: str, comment_text: str) -> dict:
    youtube_video["comments"].append({"username": username, "comment": comment_text})
    return youtube_video

def similarity_to_video(video_a: dict, video_b: dict) -> float:
    pct = 0
    return [(pct := pct + 0.2)if h in video_b["hashtag"]else(pct) for h in video_a["hashtag"]][-1]

video = create_youtube_video("test", "example", ["a", "b", "c", "d", "e", "f"])
print("say the number of likes you'd like to add")

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

for i in range(int(r.recognize_google(audio))):
    like(video)
print(video)
video_b = create_youtube_video("example", "test", ["c", "d", "e", "f", "g"])
print(video_b)
print(similarity_to_video(video, video_b))
