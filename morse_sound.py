# This file generates the morse code dits and dahs sounds
# as base 64 encoded strings for use in the HTML5/Javsacript page
import base64
from io import BytesIO
import numpy as np
import struct 
import wave

# Code based off of this answer http://stackoverflow.com/a/33246354/2574639
def sine_samples(freq, duration, framerate=44100, amplitude=0.5):
  # Get (sample rate * duration) samples on X axis 
  # (between freq oscillations of 2pi)
  X = (2*np.pi*freq/framerate) * np.arange(framerate*duration)

  # Get sine values for these X axis samples (as integers)
  S = (amplitude*32767*np.sin(X)).astype(int)

  # Pack integers as signed "short" integers (-32767 to 32767)
  as_packed_bytes = (map(lambda v:struct.pack('h',v), S))
  return as_packed_bytes

def output_wave(path, frames, framerate=44100):
  with wave.open(path,'w') as output:
    # Set parameters for output WAV file
    # (1 channel, 2 bytes per sample, framerate, num frames, no compression, no compression)
    output.setparams((1,2,framerate,0,'NONE','not compressed'))
    output.writeframes(frames)

def output_sound(path, freq, dur, framerate=44100):
  # join the packed bytes into a single bytes frame
  frames = b''.join(sine_samples(freq,dur, framerate))

  # output frames to file
  output_wave(path, frames, framerate)

def output_base64(freq, dur, framerate=44100):
  """Return Base 64 encoded string of wave file"""
  data_buffer = BytesIO()
  output_sound(data_buffer, freq, dur, framerate)
  return base64.b64encode(data_buffer.getvalue())


# We'll use a low 4.41khz framerate for our audio to reduce the string length
framerate = 4410
beep_freq = 800 # Hz
beep_duration = 0.1 # seconds

# # We could just write a wav file directly
# output_sound('dit.wav', 800, beep_duration, framerate)
# output_sound('dah.wav', 800, beep_duration*3, framerate)

# Instead of writing to file, and then reading from file to convert to base64
# We'll keep it in memory using ByteIO

dit_b64 = output_base64(beep_freq, beep_duration, framerate)
dah_b64 = output_base64(beep_freq, beep_duration*3, framerate)
# Write to text file for usage with html5 web audio
with open('dit_base64.txt','w') as f:
  f.write(dit_b64.decode('utf8'))
with open('dah_base64.txt','w') as f:
  f.write(dah_b64.decode('utf8'))

# Alternatively print to console
print("Dit (%d):\n%s" % (len(dit_b64), dit_b64.decode('utf8')))
print("Dah (%d):\n%s" % (len(dah_b64), dah_b64.decode('utf8')))

# These base64 strings can be directly used to make sound
# in an HTML5 page via javascript using:
# 
#     var snd = new Audio("data:audio/wav;base64,<base64_encoded_wav_string>")
#     snd.play()