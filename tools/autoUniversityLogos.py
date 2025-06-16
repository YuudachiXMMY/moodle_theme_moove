import os
import shutil
from PIL import Image

cwd = os.getcwd()
parent = os.path.abspath(os.path.join(cwd, os.pardir))
path = cwd + "/pix/o"
dest = cwd + "/pix/university_logo"

files = os.listdir(path)

HTML = ''
CSS = ''

def main():
    filenames = renameFiles()

    print(HTML)
    print(CSS)


def renameFiles():
    filenames = []
    for count, file in enumerate(os.listdir(path)):
        count = count + 1

        filename = "logo" + str(count) + ".png"
        filenames.append(file)

        printHTML(filename, count)

        if file.endswith(".jpg"):
            im = Image.open(path + "/" + file)
            im.save(dest + "/" + filename)
        else:
            shutil.copy2(os.path.join(path, file), os.path.join(dest, filename))

    return filenames

def printHTML(filename, count):
    global HTML, CSS
    HTML += f'<img src=\"https://www.tiaschools.online/theme/moove/pix/university_logo/{filename}\" alt=\"University Logo {count}\"  class=\"marquee__item\" width=\"125\" height=\"125\">\n'

    CSS += f'.marquee--8 .marquee__item:nth-of-type({count}) ' + '{-' + f'-marquee-item-index: {count};' + '}' + '\n'

# Driver Code
if __name__ == '__main__':
    main()