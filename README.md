# HandsomeWare (v0.9.2)
It is what it is.

## Project home
```
https://github.com/lord-aceldama/HandsomeWare
```

## Requirements
- python 3.3 or greater
- pyAesCrypt (pip) v0.4.3 or compatible

## License
Standard [MIT license](/LICENSE)

## Setup
### ./run-venv.sh ()
To set up, just run `bash run-venv.sh` which will automatically run `setup-venv.sh`. After that you can run the script
using `./run-venv.sh`.

### Global setup (No venv)
If you don't want to use a virtual environment, run the following:
```sh
pip install -r requirements.txt
chmod +x *.sh
chmod +x *.py
```

## Usage
Running `./run-venv.sh` or `./handsomeware.py` (depending on your setup) will show the help screen:
```
    )                                                            
 ( /(             (                      (  (                    
 )\())   )        )\ )          )     (  )\))(   '   ) (     (   
((_)\ ( /(  (    (()/((   (    (     ))\((_)()\ ) ( /( )(   ))\  
 _((_))(_)) )\ )  ((_))\  )\   )\  '/((_)(())\_)())(_)|()\ /((_) 
| || ((_)_ _(_/(  _| ((_)((_)_((_))(_)) \ \((_)/ ((_)_ ((_|_))   
| __ / _` | ' \)) _` (_-< _ \ '  \() -_) \ \/\/ // _` | '_/ -_)  
|_||_\__,_|_||_|\__,_/__|___/_|_|_|\___|  \_/\_/ \__,_|_| \___|  
                                                         ( v0.9.2 )


PROJECT HOME:  https://github.com/lord-aceldama/HandsomeWare    

GENERAL:
    ./handsomeware.py --help     : Show this help message.
    ./handsomeware.py --version  : Prints the current version of the script.
    
DECRYPTION:
    ./handsomeware.py --decrypt <inputfile> <outputfile>

ENCRYPTION
    ./handsomeware.py [flags] <path>

    Flags:
        --shred [passes]  : Shred files after encryption. Use passes to specify
                            how many times to overwrite files. (Default: 1)
        --ssd             : Use this flag if the file/directory is on a drive
                            that does rotational writes. If you are unsure,
                            check [ https://unix.stackexchange.com/a/65602 ].
        --x <ext>[,<ext>] : Only encrypt files with extension <ext>. Multiple 
                            extensions can be given by separating them with ",".
        --rnd [len]       : Use random password of length [len]. (Default: 20)
```

## Update
To update the script to the latest version, run `./update.sh`.

# Donations
Every bit helps keep me motivated.

### XMR:
```
49urDtJ4Fp7M6aa8fN7UabLjhxcvcgYXLSeDcjLDcYsLRB1FJJzrYTARHLNwqT4DdVLxjycZ9L9aPj3SCrhhqR2AQAyLrNd
```

You can also donate XMR for free by [pool mining](https://web.xmrpool.eu/xmr-monero-easy-mining-guide.html#callout-progress-mining) for a few days.
```
xmrig --coin 'monero' -o xmrpool.eu:5555 -u 49urDtJ4Fp7M6aa8fN7UabLjhxcvcgYXLSeDcjLDcYsLRB1FJJzrYTARHLNwqT4DdVLxjycZ9L9aPj3SCrhhqR2AQAyLrNd+handsomeware -p x
```

# Changelog
### 0.9.2 (2020-11-11)
- Added csv functionality to `--x` flag.

### 0.9.1 (2020-11-10)
- Added `--ssd` flag to ensure secure shred writes over files on media with rotational writes.
- Added `--version` flag.
- Added `passes` parameter to `--shred` flag.
- Added `setup-venv.sh` and `run-venv.sh` scripts to make using virtual environments simpler.

### 0.9.0 (2020-10-27)
- Published alpha build

