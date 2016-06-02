from __future__ import print_function
from wand.image import Image

with Image(filename='source.pdf') as img:
    print('width =', img.width)
    print('height =', img.height)
    print('pages = ', len(img.sequence))
    print('resolution = ', img.resolution)

    with img.convert('png') as converted:
        converted.save(filename='pyout/page.png')
