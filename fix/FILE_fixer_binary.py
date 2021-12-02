import os
from pathlib import Path
from shutil import copyfile


def cue_action(cue, audio_name, audio_ext):

    try:
        opened_cue = open(cue, 'rb')
    except:
        print("Couldn't open " + cue)
    with opened_cue:
        search = bytes(audio_name.encode()) + bytes(audio_ext.encode())
        for line in opened_cue:
            if search not in line and b'FILE "' in line:
                file_line = line
                opened_cue.seek(0)
                data = opened_cue.read()
                opened_cue.close()

                start = file_line.find(b'FILE "') + len(b'FILE "')
                end = file_line.rfind(b'"')
                cue_file_entry = file_line[start:end]

                bak = 1
                try:
                    copyfile(cue, cue + '.bak')
                except:
                    print("Could not backup, no action has been taken on " + cue)
                    bak = 0

                if bak:

                    try:
                        opened_cue = open(cue, 'wb')
                    except:
                        print("cue backup created but couldn't open " + cue)
                    with opened_cue:
                        data = data.replace(cue_file_entry, search)
                        opened_cue.write(data)
                        opened_cue.close()
                        return True
                break

        opened_cue.close()
        return False



for root, dirs, files in os.walk('C:\\Users\\Carlo\\test'):

    audio_ext = None
    audio_name = None

    for f in files:
        if audio_ext is None and (f.endswith(".flac") or f.endswith(".ape") or f.endswith(".wv") or f.endswith(".wav") or f.endswith(".wavpack") or f.endswith(".FLAC") or f.endswith(".APE") or f.endswith(".WV") or f.endswith(".WAV") or f.endswith(".WAVPACK") or f.endswith(".Flac")):
            audio_ext = Path(f).suffix
            audio_name = Path(f).stem

    if audio_ext is not None:
            for f in files:
                if f.endswith(".cue") or f.endswith(".CUE"):
                    cue = os.path.join(root, f)
                    if cue_action(cue, audio_name, audio_ext):
                        print(root)
                        #print(cue)
                    #break
