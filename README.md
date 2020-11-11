# HandsomeWare
It is what it is.

# Project home (v0.9.1)
```
https://github.com/lord-aceldama/HandsomeWare
```

# Requirements
- python 3.3 or greater
- pyAesCrypt (pip) v0.4.3 or compatible

# Donations
XMR:
```
49urDtJ4Fp7M6aa8fN7UabLjhxcvcgYXLSeDcjLDcYsLRB1FJJzrYTARHLNwqT4DdVLxjycZ9L9aPj3SCrhhqR2AQAyLrNd
```

# Usage
```
    )                                                            
 ( /(             (                      (  (                    
 )\())   )        )\ )          )     (  )\))(   '   ) (     (   
((_)\ ( /(  (    (()/((   (    (     ))\((_)()\ ) ( /( )(   ))\  
 _((_))(_)) )\ )  ((_))\  )\   )\  '/((_)(())\_)())(_)|()\ /((_) 
| || ((_)_ _(_/(  _| ((_)((_)_((_))(_)) \ \((_)/ ((_)_ ((_|_))   
| __ / _` | ' \)) _` (_-< _ \ '  \() -_) \ \/\/ // _` | '_/ -_)  
|_||_\__,_|_||_|\__,_/__|___/_|_|_|\___|  \_/\_/ \__,_|_| \___|  


DECRYPTION:
    ./handsomeware.py --decrypt <inputfile> <outputfile>

ENCRYPTION
    ./handsomeware.py [flags] <path>

    Flags:
        --help            : Show this help message
        --shred [passes]  : Shred files after encryption. Use passes to specify
                            how many times to overwrite files. (Default: 1)
        --ssd             : Use this flag if the file/directory is on a drive
                            that does rotational writes. If you are unsure,
                            check [ https://unix.stackexchange.com/a/65602 ].
        --x <ext>         : only encrypt files with extension .ext
        --rnd <len>       : generate random password of length "len"
```

# Changelog
## 0.9.1 (2020-11-10)
- Added `passes` parameter to `--shred` flag
- Added `--ssd` flag to ensure secure shred writes over files on media with rotational writes.

## 0.9.0 (2020-10-27)
- Published alpha build