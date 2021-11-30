import os

#  cut a 1 minute clip
os.system("ffmpeg -ss 00:00:00 -i bbb_original.mp4 -c copy -t 00:01:00.0 bbb_1min.mp4".format("mp4"))

#we extract the audio in mp3
os.system("ffmpeg -i bbb_1min.mp4 -codec:a libmp3lame -qscale:a 2 bbb_audio.mp3")

#we extract the audio in aac with 16K bitrate
os.system("ffmpeg -i bbb_1min.mp4 -b:a 16k -vn bbb_audio_bitrate.aac")

#we package into a container
os.system("ffmpeg -i bbb_1min.mp4 -i bbb_audio.mp3 -i bbb_audio_bitrate.aac -c:v copy -c:a copy -c:a copy -f mp4  container.mp4")