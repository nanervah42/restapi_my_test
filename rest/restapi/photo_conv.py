from PIL import Image


def watermark_with_transparency(input_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = '..\media\watermarks\watermark1.png'
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    return transparent
    # transparent.show()
    # transparent.save(output_image_path)


if __name__ == '__main__':
    img = '..\media\watermarks\\testimg.jpg'


    watermark_with_transparency(img, position=(0, 0))