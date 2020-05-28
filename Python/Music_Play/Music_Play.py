from pygame import mixer
import time
file = r"E:\Git_Repositories\song.mp3"
mixer.init()
mixer.music.load(file)
mixer.music.play()
time.sleep(10)
mixer.music.stop()
