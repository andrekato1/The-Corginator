from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap

class Drawer():
    def __init__(self):
        self.img = Image.open('corgis\\1.jpeg')
        self.x, self.y = self.img.size

    def draw_text(self, text):
        font = ImageFont.truetype("impact.ttf", 68)
        draw = ImageDraw.Draw(self.img)
        y_text = self.y*0.68
        lines = textwrap.wrap(text, width=70)
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text(((self.x - line_width) / 2, y_text), 
                    line, font=font, fill=(255, 255, 255))
            y_text += line_height
        self.img.save("corgis\\out.jpeg")
