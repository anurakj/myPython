from mingus.midi import fluidsynth

import time

fluidsynth.init("DrawnToLife2.sf2")

fluidsynth.play_Note(64)

time.sleep(1)

fluidsynth.play_Note(65)


