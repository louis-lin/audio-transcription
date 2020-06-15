from __future__ import unicode_literals
# Recieve Youtube link as input
#LINK = 'https://www.youtube.com/watch?v=dF3Dcol5XLg'
LINK = 'https://www.youtube.com/watch?v=-122SRX3sbI'
#LINK = 'https://www.youtube.com/watch?v=_I7uGjDJ0lM'

# Download Youtube Video as Audio file
import youtube_dl
options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "wav",  # convert to wav
  'outtmpl': '%(title)s',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}

#with youtube_dl.YoutubeDL(options) as ydl:
#   ydl.download([LINK])

# Convert the wav file
import ffmpeg
(ffmpeg
.input('The Benefits of Crying')
.output('test%02d.wav',f='segment',segment_time='30')
.run(cmd='/usr/local/Cellar/ffmpeg/4.2.3/bin/ffmpeg')
)

# Tanscribe audio file                                                         
import speech_recognition as sr
import glob
import os
Transcript = open('Transcription.txt','w')
r = sr.Recognizer()
files = glob.glob("*.wav")
files.sort()

for audio_file in files:
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # read the entire audio file                  
        #print("Transcription for " +os.path.splitext(audio_file)[0]+':  ' r.recognize_google(audio))
        text = r.recognize_google(audio)
        Transcript.write(text)
        print(text)
Transcript.close()
