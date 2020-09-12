# random-playlist
Python script for Volumio to generate random songs playlists.

This script generate random Volumio playlist to folder `/data/playlist` from all of your library. 

# Version

0.3

# Dependencies

* `python3`

# Usage

`./python3 random-playlist.py /mnt/NAS/[yourNASname]`
```
-h, --help - Show help 
-v, --version - Show version 
-p, --playlist-file - Destination file (Default: /data/playlist/random)
-n - Number of tracks to generate (Default: 50)
-d, --debug - Write parsed items
```

# Install

Copy file `random-playlist.py` to `/home/volumio/`

For right function must be locales set to UTF-8. 

`dpkg-reconfigure localses`

and select your language and UTF-8

Recomended is added to cron. 

`crontab -e`

add line

`50 23 * * * python3 /home/volumio/random-playlist.py /mnt/NAS/[yourNASname]`

This command start random-playlist.py every day in 23:50

# Example

`./python3 random-playlist.py /mnt/NAS/[yourNASname]`

Usual use of this script. Browse library and add 50 .FLAC or .DSF files to playlist random in folder /data/playlist/. 
