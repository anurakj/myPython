from pyfluidsynth3 import fluidaudiodriver, fluidhandle, fluidsettings, fluidsynth
import time

handle = fluidhandle.FluidHandle( 'libfluidsynth.dll' )
settings = fluidsettings.FluidSettings( handle )
synth = fluidsynth.FluidSynth( handle, settings )
synth.load_soundfont( 'Full Grand.sf2' )
driver = fluidaudiodriver.FluidAudioDriver( handle, synth, settings )

synth.noteon( 0, 78, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 78 )


synth.noteon( 0, 78, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 78 )


synth.noteon( 0, 85, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 85 )

synth.noteon( 0, 85, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 85 )

synth.noteon( 0, 87, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 87 )

synth.noteon( 0, 87, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 87 )

synth.noteon( 0, 85, 1.0 )
time.sleep( 1 )
synth.noteoff( 0, 85 )
