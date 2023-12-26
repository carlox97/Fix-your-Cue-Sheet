import os

for root, dirs, files in os.walk(os.getcwd()):

    cue = 0
    audio_files = 0

    for f in files:
        if f.lower().endswith(".cue"):
            cue += 1
        elif f.lower().endswith((".flac", ".ape", ".wv", ".wav", ".wavpack")): 
            audio_files += 1

    if cue > 1 or (cue == 1 and audio_files != 1):
        print(root)
        #cuepath = os.path.join(root, f)
        #print(cuepath)
