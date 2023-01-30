import os
from pathlib import Path


def cue_action(cue, audio_name, audio_ext):

    try:
        opened_cue = open(cue, 'r',errors='ignore', encoding='utf-8')
    except:
        print("Couldn't open " + cue)
    with opened_cue:
        search = audio_name + audio_ext
        if search in opened_cue.read():
            opened_cue.close()
            return False

        opened_cue.close()
        return True


cwd = os.getcwd()

for root, dirs, files in os.walk(cwd):

    audio_ext = None
    audio_name = None

    for f in files:
        if audio_ext is None and (f.endswith(".flac") or f.endswith(".ape") or f.endswith(".wv") or f.endswith(".wav") or f.endswith(".wavpack") or f.endswith(".FLAC") or f.endswith(".APE") or f.endswith(".WV") or f.endswith(".WAV") or f.endswith(".WAVPACK") or f.endswith(".Flac")):
            audio_ext = Path(f).suffix
            audio_name = Path(f).stem

    if audio_ext is not None:
            for f in files:
                if f.endswith(".cue") or f.endswith(".CUE") or f.endswith(".Cue"):
                    cue = os.path.join(root, f)
                    if cue_action(cue, audio_name, audio_ext):
                        print(root)
                        #print(cue)
                    #break
