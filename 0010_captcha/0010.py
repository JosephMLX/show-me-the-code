from PIL import Image, ImageDraw, ImageFont, ImageFilter
from random import randrange, randint

width = 240
height = 60
candidate = ''
background_color = (255, 255, 255)
for i in range(65, 91):
    candidate += chr(i)
for i in range(97, 123):
    candidate += chr(i)
for i in range(48, 58):
    candidate += chr(i)


def generate_captcha_code(cadidate_str):
    captcha_code = ''
    for _ in range(4):
        index = randrange(len(cadidate_str))
        captcha_code += cadidate_str[index]
    return captcha_code


def random_background_color():
    return (randint(64, 255),
            randint(64, 255),
            randint(64, 255))


def random_code_color():
    return (randint(32, 127),
            randint(32, 127),
            randint(32, 127))


def generate_captcha_pic(captcha_code):
    image = Image.new('RGB', (width, height), background_color)
    font = ImageFont.truetype("Monaco.dfont", size=36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=random_background_color())
    for i in range(len(captcha_code)):
        draw.text((60 * i + 10, 10), captcha_code[i], font=font, fill=random_code_color())
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == "__main__":
    captcha_code = generate_captcha_code(candidate)
    generate_captcha_pic(captcha_code)
