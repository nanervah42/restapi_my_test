# from PIL import Image
#
#
# def watermark_with_transparency(input_image_path,
#                                 position):
#     base_image = Image.open(input_image_path)
#     watermark = '..\media\watermarks\watermark1.png'
#     width, height = base_image.size
#     transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
#     transparent.paste(base_image, (0, 0))
#     transparent.paste(watermark, position, mask=watermark)
#     transparent.show()
#     transparent.save('..\media\watermarks\\testimg_done.jpg')
#
#
# if __name__ == '__main__':
#     img = '..\media\watermarks\\testimg.jpg'
#
#
#     watermark_with_transparency(img, position=(0, 0))

from PIL import Image

from rest.settings import MEDIA_ROOT


def watermark_with_transparency(input_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(MEDIA_ROOT / 'watermark1.png')
    width, height = base_image.size

    base_image = base_image.convert("RGB")
    transparent = Image.new('RGB', (width, height), (0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, (0, 0), mask=watermark)
    # transparent.show()
    transparent.save(input_image_path)


if __name__ == '__main__':
    img = '..\media\watermarks\\del.jpg'
    watermark_with_transparency(img)