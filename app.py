from PIL import Image
import os

print("started>>>>>>>>>>>>>>")
repo_path = os.getcwd()
def convert(inPath, outPath):
    for root, dirs, files in os.walk(inPath):
        for file in files:
            file_path = inPath = os.path.join(root, file)
            img = Image.open(file_path)
            output_path = os.path.join(root, os.path.splitext(file)[0] + ".png")
            img.save(output_path, "PNG")
            print("image saved")


inPath = os.path.join(repo_path, 'data') 
outPath = os.path.join(repo_path, 'data')

convert(inPath, outPath)