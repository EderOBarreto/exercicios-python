from time import sleep
from pygame import mixer

mixer.init()
mixer.music.load('ex046.mp3')

print(10 * '=' + 'contagem regressiva' + 10 * '=')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
mixer.music.play(0)
sleep(5)

