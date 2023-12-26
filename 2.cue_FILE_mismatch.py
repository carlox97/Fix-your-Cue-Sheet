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
        if f.lower().endswith(".cue"):
            cue = os.path.join(root, f)
            for g in files:
                if audio_ext is None and (g.lower().endswith((".flac", ".ape", ".wv", ".wav", ".wavpack"))):    
                    audio_ext = Path(g).suffix
                    audio_name = Path(g).stem
            if audio_name is not None and cue_action(cue, audio_name, audio_ext):
                print(root)
                #print(cue)
                #break
