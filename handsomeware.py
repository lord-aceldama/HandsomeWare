#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import random

try:
    import pyAesCrypt
except ImportError:
    print("Error importing pyAesCrypt. Please run 'pip install pyAesCrypt'.")
    sys.exit(-1)

VERSION = "0.9.2"
BUFFER_SIZE = 64 * 1024
DEFAULT_PASSWORD = None  # if you want you can use a string like "Password123" here.


# ---------------------------------------------------------------------
def print_splash():
    """Prints a splash screen."""
    print(f"""
    )                                                            
 ( /(             (                      (  (                    
 )\\())   )        )\\ )          )     (  )\\))(   '   ) (     (   
((_)\\ ( /(  (    (()/((   (    (     ))\\((_)()\\ ) ( /( )(   ))\\  
 _((_))(_)) )\\ )  ((_))\\  )\\   )\\  '/((_)(())\\_)())(_)|()\\ /((_) 
| || ((_)_ _(_/(  _| ((_)((_)_((_))(_)) \\ \\((_)/ ((_)_ ((_|_))   
| __ / _` | ' \\)) _` (_-< _ \\ '  \\() -_) \\ \\/\\/ // _` | '_/ -_)  
|_||_\\__,_|_||_|\\__,_/__|___/_|_|_|\\___|  \\_/\\_/ \\__,_|_| \\___|  
                                                         ( v{VERSION} )
""")


def print_help():
    """Prints the help menu."""
    script = os.path.basename(sys.argv[0])
    print(f"""
PROJECT HOME:  https://github.com/lord-aceldama/HandsomeWare    

GENERAL:
    ./{script} --help     : Show this help message.
    ./{script} --version  : Prints the current version of the script.
    
DECRYPTION:
    ./{script} --decrypt <inputfile> <outputfile>

ENCRYPTION
    ./{script} [flags] <path>

    Flags:
        --shred [passes]  : Shred files after encryption. Use passes to specify
                            how many times to overwrite files. (Default: 1)
        --ssd             : Use this flag if the file/directory is on a drive
                            that does rotational writes. If you are unsure,
                            check [ https://unix.stackexchange.com/a/65602 ].
        --x <ext>[,<ext>] : Only encrypt files with extension <ext>. Specify 
                            more than one by separating extensions with a comma.
        --rnd [len]       : Generate random password of length [len].

""")


def get_random_string(length):
    """Gets a random string of specified length."""
    sample_letters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join([random.choice(sample_letters) for _ in range(length)])


def create_file(path):
    """Creates a temporary file and returns the name and disk free space."""
    result = None, 0
    # Get tempfile name
    try:
        # Get temp file name
        filename = '.'
        while os.path.exists(filename):
            filename = os.path.join(path, get_random_string(32))

        # Create temp file
        f = open(filename, "wb")
        f.close()

        # Get disk free space
        statvfs = os.statvfs(path)
        free_bytes = statvfs.f_frsize * statvfs.f_bavail

        result = filename, free_bytes

    except Exception as e:
        # Something went wrong
        print(f"ERROR: {e}")

    return result


def lock_free_space(path):
    """Creates a file (or files, if df > 1GB) filling all free disk space.

    disk free:  https://stackoverflow.com/a/39799743
    fast write: https://stackoverflow.com/a/8816144
    """
    result = []
    filename, free_bytes = create_file(path)
    while (filename is not None) and (free_bytes > 0):
        result.append(filename)

        f = open(filename, "wb")
        f.seek(min(2 ** 30, free_bytes) - 1)
        f.write(b"\0")
        f.close()

        filename, free_bytes = create_file(path)
    return result


def secure_delete(file_path, passes=1, ssd=False):
    """Fast file shredder."""
    lock_files = lock_free_space(os.path.dirname(file_path)) if ssd else []

    with open(file_path, "ba+") as del_file:
        length = del_file.tell()
        for i in range(passes):
            del_file.seek(0)
            del_file.write(os.urandom(length))
    os.remove(file_path)

    for lock_file in lock_files:
        os.remove(lock_file)


def get_filename(file_path, filename):
    """Makes sure the file doesn't exist."""
    result = f"{filename}.aes"
    i = 0
    while os.path.exists(os.path.join(file_path, result)):
        i = i + 1
        result = f"{filename}_{i}.aes"
    return result


def get_password():
    """Gets a password and make sure you type it correctly, twice."""

    def twice():
        """Asks for pass."""
        return input("Enter password: "), input("Re-enter password: ")

    result, verify = twice()
    while result != verify:
        print("Password mismatch, please try again.")
        result, verify = twice()
    return result


def do_encrypt():
    """."""
    password = DEFAULT_PASSWORD
    root_dir = sys.argv[-1]
    if os.path.exists(root_dir):
        # Get command line flags
        ext = None
        if "--x" in sys.argv:
            ext = sys.argv[sys.argv.index("--x") + 1].split(",")
            print(f" * Encrypting all files with extension(s): {', '.join(ext)}")

        shred_originals = "--shred" in sys.argv
        shred_passes = 1
        if shred_originals:
            try:
                shred_passes = int(sys.argv[sys.argv.index("--shred") + 1])
            except:
                shred_passes = 1
            print(f" * Shredding originals after encryption. ({shred_passes} passes)")

        if "--rnd" in sys.argv:
            try:
                password = get_random_string(int(sys.argv[sys.argv.index("--x") + 1]))
            except:
                print(" * Attempted to get password length but failed. Defaulting to 20 chars.")
                password = get_random_string(20)
            print(f" * Random password generated: {password}")

        # Get password, if not set
        if password is None:
            password = get_password()

        # Set SSD flag
        is_ssd = "--ssd" in sys.argv

        # Nuke!
        for path, _, files in os.walk(root_dir):
            print(f"[{path}]")
            for infile in files:
                f_ext = os.path.splitext(infile)[1]
                if (ext is None) or (f_ext == "") or (f_ext[1:] in ext):
                    outfile = os.path.join(path, get_filename(path, infile))
                    print(f"  + {infile} -> {outfile}")
                    try:
                        pyAesCrypt.encryptFile(os.path.join(path, infile), outfile, password, BUFFER_SIZE)
                        if shred_originals:
                            print(f"    >> Shredding...")
                            secure_delete(os.path.join(path, infile), shred_passes, is_ssd)
                    except Exception as e:
                        print(f"    >> Error: {e}")
    else:
        print("Error: The path could not be found!")


def do_decrypt():
    """."""
    if len(sys.argv) == 4:
        file_in = sys.argv[2]
        file_out = sys.argv[3]
        if not os.path.exists(file_in):
            print(f"Error: Could not find file '{file_in}.'")
        elif os.path.isdir(file_in):
            print(f"Error: File expected but '{file_in}' is a directory.")
        elif os.path.exists(file_out):
            print(f"Error: File '{file_in}' already exists.'")
        else:
            password = input("Password: ") if DEFAULT_PASSWORD is None else DEFAULT_PASSWORD
            print("Decrypting...")
            pyAesCrypt.decryptFile(file_in, file_out, password, BUFFER_SIZE)
    else:
        print(f"Error: Expected 3 command line args but got {len(sys.argv) - 1}.")
        print_help()


# ---------------------------------------------------------------------
print_splash()
if "--version" in sys.argv:
    print(VERSION)
if (len(sys.argv) == 1) or ("--help" in sys.argv):
    print_help()
else:
    if "--decrypt" in sys.argv:
        do_decrypt()
    else:
        do_encrypt()
    print("\nAll tasks failed successfully. Have a nice day :)\n\n")
