# written by Joseph Meng 2018
# mlx7.xyz

from PIL import Image, ImageDraw, ImageFont, ImageColor


def main():
    try:
        # pic relative path
        img = Image.open("picture.jpg")
        # save rotated pic
        # img = img.rotate(180)
        # img.save("rotated_picture.jpg")
        # draw a red circle
        draw = ImageDraw.Draw(img)
        # TODO
        # draw a red circle with white text inside, like Wechat moment
        # circle = ImageDraw.ellipse((20, 20, 180, 180), fill='red', outline='red')
        # img.paste(circle, (50, 50))
        my_font = ImageFont.truetype("Monaco.dfont", size=100)
        my_color = "red"
        width, height = img.size
        draw.text((width-100, 50), "7",
                  font=my_font, fill=my_color)
        img.save("edited_picture.jpg")
        return
    except IOError:
        pass


if __name__ == "__main__":
    main()