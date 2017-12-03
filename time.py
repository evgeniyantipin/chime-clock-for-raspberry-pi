import threading
import pyglet.media as pg
from datetime import datetime

def check_time():
    ctime = datetime.now().time().strftime("%I:%M:%S")
    if ctime[3:] == "00:00":
        src = "/home/pi/Desktop/chimes/chime.wav"
        chime = pg.load(src, streaming=False)
        player = pg.Player()
        player.volume = 0.5
        for h in range(int(ctime[:2])):
            player.queue(chime)
        player.play()
    threading.Timer(1, check_time).start() #runs check_time every 1 sec

check_time()
