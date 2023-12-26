
# Fix-your-Cue-Sheet
Collection of simple python scripts to deal with .cue files and their problems.

## Usage

Install Python, place the scripts to your desired folder (eg. root of your music library), open a command line interface within that folder and run `python 1.cue_conflict_folder.py`

## 1.cue_conflict_folder.py

It checks *folders* and *sub-folders* within the desired folder for the following (**unwanted**) conditions:
- folder contains one .cue and no audio files
- folder contains one .cue and more than one audio file
- folder contains more than one .cue file

Then it lists these problematic folders, so you can manually fix them. This is useful if you want your music folders to contain one .cue file and one audio file only. 

   
## 2.cue_FILE_mismatch.py
Occasionally cue files point to a .wav file even though your audio file is actually .flac/.ape/.etc AND/OR the cue points to an audio file named differently from the one you have in your folder and that's bad: your audio player won't be able to play that cue unless the correct filename is specified

This should be the second tool to use, since it is **useful if you only have one .cue and one audio file per folder in your library** : the goal is to check whether the audio file *my_cd.flac* is present in the `FILE "my_cd.flac" WAVE` line in the cue file, for each folder and sub-folder. It folders containing such problematic .cue files.

## **FILE_fixer.py (not recommended)**
**only useful if you have ONLY one .cue and one audio file per folder in your library, do NOT run otherwise**
For each folder and sub-folder in your path this tool search for *your_audio_file.flac/ape/etc* in the cuesheet. If it's not present in the , it replaces 
 `FILE "whatever.whatever" WAVE` 
 with 
 `FILE "your_audio_file.flac" WAVE` 

and shows the foder containing the cue that was replaced.

 Before doing such replacement it creates a copy of your cue in the same folder. 
 **BE CAREFUL**: if you run this more than once the backup cue will be overwritten with a backup of the new cue and this will result with the loss of your original cue.

