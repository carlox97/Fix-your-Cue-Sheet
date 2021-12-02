# Fix-your-Cue-Sheet
Python tools to deal with .cue files that are not properly configured.

## cue_conflict_folder

This should be the first tool to be be used: it shows path to *folders* and *sub-folders* within the specified path when the following (unwanted) conditions are satisfied:
- folder contains one .cue and no audio files
- folder contains one .cue and more than one audio files
- folder contains more than one .cue file

This is useful if you only want your CD folders to contain one .cue file and one audio file. This is a must if you plan to split a multi-disc flac with foobar or similar and there are no tags for *discnumber*, and it happens to be the case for most .cue files. Otherwise you'll have in the same folder as much 

    01.Title
    01.Title

 tracks as the number of discs in the multi-disc CDs, making it hard to recognize the CD number they belong to.


