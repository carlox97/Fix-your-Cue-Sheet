import os


cwd = os.getcwd()

for root, dirs, files in os.walk(cwd):

    cue = 0
    audio_files = 0

    for f in files:
        if f.endswith(".cue") or f.endswith(".CUE") or f.endswith(".Cue"):
            cue += 1
        elif f.endswith(".flac") or f.endswith(".ape") or f.endswith(".wv") or f.endswith(".wav") or f.endswith(".wavpack") or f.endswith(".FLAC") or f.endswith(".APE") or f.endswith(".WV") or f.endswith(".WAV") or f.endswith(".WAVPACK") or f.endswith(".Flac"):
            audio_files += 1

    if cue > 1 or (cue == 1 and audio_files != 1):
        print(root)
        #cuepath = os.path.join(root, f)
        #print(cuepath)
