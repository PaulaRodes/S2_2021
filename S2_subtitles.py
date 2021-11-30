import os

#I tried to extract the subtitles from the original video but the mp4 does not contain the subtitles
#os.system("ffmpeg -i bbb_original.mp4 subs.srt")

# we add the subtitles to the 1 minute clip
os.system("ffmpeg -i bbb_1min.mp4 -i subtitles.srt -c copy -c:s mov_text bbb_subtitles.mp4")