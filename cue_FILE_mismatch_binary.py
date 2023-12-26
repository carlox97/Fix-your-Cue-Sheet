import os
from pathlib import Path


def cue_action(cue, audio_name, audio_ext):
   marks = "\""
   search = bytes(marks.encode()) + bytes(audio_name.encode()) + bytes(audio_ext.encode()) + bytes(marks.encode())

   try:
       with open(cue, 'rb') as opened_cue:
           for line in opened_cue:
               if search in line:
                  return False
   except:
       print("Couldn't open " + cue)

   return True


for root, dirs, files in os.walk(os.getcwd()):

    audio_ext = None
    audio_name = None

    for f in files:
        if audio_ext is None and (f.lower().endswith((".flac", ".ape", ".wv", ".wav", ".wavpack"))):    
            audio_ext = Path(f).suffix
            audio_name = Path(f).stem

    if audio_ext is not None:
            for f in files:
                if f.lower().endswith(".cue"):
                    cue = os.path.join(root, f)
                    if cue_action(cue, audio_name, audio_ext):
                        print(root)
                        #print(cue)
                    #break
