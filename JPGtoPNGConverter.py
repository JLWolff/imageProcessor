import sys
import os
from PIL import Image

arguments = sys.argv

try:
    in_folder = arguments[1]
    out_folder = arguments[2]
except IndexError as err:
    print("Please enter the in and the out folder")

files_to_convert = map(lambda file: os.path.join(in_folder, file),os.listdir(in_folder))

for infile in files_to_convert:
    f = os.path.basename(os.path.splitext(infile)[0]) 
    outfile = out_folder + f + ".png"
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile, 'png')
                print(f"All done {f}")
        except OSError as err:
            print("cannot convert", infile)