from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import json

def read_config():
    # Example Configs:
    # {
    #     "videoPath" : "dialogues.mp4",
    #     "titleText" : "Top 3:\n\nDialogues Of All Time",
    #     "outputFilename": "output.mp4",
    #     "captions" : [
    #         {"caption": "Mr India (1987)\nAmrish Puri", "time": 0},
    #         {"caption": "Sholay (1975)\nAmjad Khan", "time": 6},
    #         {"caption": "Don (1978)\nAmitabh Bachchan", "time": 25}
    #     ]
    # }

    # {
    #     "videoPath" : "songs.mp4",
    #     "titleText" : "Who Said It Better?\n\nYou Decide!",
    #     "outputFilename": "output.mp4",
    #     "captions" : [
    #         {
    #             "caption": "Zara Hatke, Zara Bachke (2023)\nTere Vaaste", 
    #             "time": 0
    #         },
    #         {
    #             "caption": "Aladin (2009)\nYou May Be",
    #             "time": 9
    #         }
    #     ]
    # }

    with open('config.json', 'r') as config:
        data = json.load(config)
        video_path = data["videoPath"]
        title_text = data["titleText"]
        output_filename = data["outputFilename"]
        captions = data["captions"]

    create_format(video_path, title_text, output_filename, captions)

def create_format(videoPath, titleText, outputFilename, captions):
    video_clip = VideoFileClip(videoPath, target_resolution=(None, 1300))
    duration = video_clip.duration

    width, height = 1080, 1920
    black_bg = ColorClip(size=(width, height), color=(0,0,0), duration=duration)

    title_txt_clip = TextClip(titleText, fontsize = 75, color = 'white', method="caption", size=(width,height/3), font="Arial")
    title_txt_clip = title_txt_clip.set_duration(duration)

    video_position = (width // 2 - video_clip.w // 2, height // 2 - video_clip.h // 2)
    video_clip = video_clip.set_position(video_position).set_duration(duration)

    text_position = ("center", 1500)

    clip_text = []
    for i in range(0,len(captions)):
        txt_clip = TextClip(captions[i]["caption"], fontsize = 60, color = 'white', method="caption", size=(width, None), font="Arial")
        if i == len(captions)-1:
            txt_clip = txt_clip.set_position(text_position).set_start(captions[i]["time"]).set_duration(duration - captions[i]["time"])
        elif i == 0:
            txt_clip = txt_clip.set_position(text_position).set_start(captions[i]["time"]).set_duration(captions[i+1]["time"])
        else:
            txt_clip = txt_clip.set_position(text_position).set_start(captions[i]["time"]).set_duration(captions[i+1]["time"] - captions[i]["time"])
        clip_text.append(txt_clip)


    composite = [black_bg, title_txt_clip, video_clip] + clip_text
    final_clip = CompositeVideoClip(composite)
    final_clip.write_videofile(outputFilename, codec="libx264", fps=30)

if __name__ == "__main__":
    read_config()
