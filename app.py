from PIL import Image
import os

def convert(inPath, outPath):
    with Image.open(inPath) as img:
        img.save(outPath, "PNG")


inPath = "img1.jpg"
outPath = "img1.png"

convert(inPath, outPath)