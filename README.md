# Fix-your-Cue-Sheet
Simple python tools to deal with .cue files.

## cue_conflict_folder

This should be the first tool to be be used: it shows *folders* and *sub-folders* within the specified path when the following (**unwanted**) conditions are satisfied:
- folder contains one .cue and no audio files
- folder contains one .cue and more than one audio file
- folder contains more than one .cue file

This is useful if you only want your music folders to contain one .cue file and one audio file, like me. I think it's a must if you plan to bulk split multi-disc releases with foobar or similar and there are no *discnumber* tags you can include in filename when performing the splitting conversion. If you do it anyway you could end up with as many

    01.Title
    01.Title
    02. Title
    02. Title
    etc.

 files as the number of discs in the multi-disc release, making it hard to recognize the CD number they belong to.
 If you are familiar with basic logic you can tweak this simple file (line 14) to just show *your* unwanted conditions. Feel free to open an issue if you tried and aren't able to...

   
## cue_FILE_mismatch.py
Occasionally cue files point to a .wav file even though your audio file is actually .flac/.ape/.etc or/and the cue points to an audio file named differently from the one you have in your folder and that's bad: your audio player won't be able to play that cue unless the correct filename is specified

This should be the second (and last recommended tool) to use. At the moment **only useful if you have no more than one .cue and one audio file per folder in your library** : the goal is to check whether the audio file *my_cd.flac* is present in the `FILE "my_cd.flac" WAVE` line in the cue file, for each folder and sub-folder in path.
It it's not present the path to the folder containing such cue will be showed (you can uncomment `print(cue)` to show the path to the cue instead of the folder)

## **FILE_fixer (not recommended)**
**only useful if you have no more than one .cue and one audio file per folder in your library, do NOT run otherwise**
For each folder and sub-folder in your path this tool search for *your_audio_file.flac/ape/etc* in the cuesheet. If it's not present in the , it replaces 
 `FILE "whatever.whatever" WAVE` 
 with 
 `FILE "your_audio_file.flac" WAVE` 

and shows the foder containing the cue that was replaced.

 Before doing such replacement it creates a copy of your cue in the same folder. 
 **BE CAREFUL**: if you run this more than once the backup cue will be overwritten with a backup of the new cue and this will result with the loss of your original cue.

## Note on text encoding and binary
Maybe last time you were in Thailand you decided to rip a disc with EAC and the generated cue and audio file have some weird characters in them. This is where the binary version of the last two tools could come in handy. Use them if you are having problems with the non-binary ones.

## Usage
Install python: be sure to check *add to PATH* during the installation, then open windows terminal and type

    python cue_conflict_folder.py

I use these tools on windows, hence the path has to be specified with  double escapes

> C:\\\Users\\\Whatever

The path is specified inside each .py file, so you have to manually edit for the tool you plan to use. You can easily do that by opening any of th eincluded files with your favorite text editor and modify the following line (which is present in all the files)

    for root, dirs, files in os.walk('G:\\'):

## Be careful!
I know how painful it is to lose precious data, so be careful if you use the FILE_fixer.py tool. After you run it once, look carefully at the output and verify that everything is ok with the replaced cue files, restore them to their original if necessary and manually fix them.

