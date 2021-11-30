import os

#video with macroblocks and motion vectors
os.system("ffmpeg -flags2 +export_mvs -i bbb_cut.mp4 -vf codecview=mv=pf+bf+bb bbb_motion.mp4")

