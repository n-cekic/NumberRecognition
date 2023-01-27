from PIL import Image


class ImagePreprocessing:
    def __init__(self, path=None):
        self.image = None

        if path is not None:
            self.open(path)

        self.new_width = 400
        self.new_height = 400
        self.cutoff = 110
        self.content_padding = 0.01

    def open(self, path):
        self.image = Image.open(path)

    def pixelate(self):
        self.image = self.image.resize((self.new_width, self.new_height))

    def to_gray(self):
        self.image = self.image.convert("L")

    def locate_content(self):
        top = 9999
        left = 9999
        right = -1
        bottom = -1
        print(f"w:%s H:%s", self.image.width, self.image.width)
        for i in range(0, self.image.height):
            for j in range(0, self.image.width):
                if self.image.getpixel((j, i)) > self.cutoff:
                    print(self.image.getpixel((j, i)))
                    continue
                if i < top:
                    top = i

                if i > bottom:
                    bottom = i

                if j < left:
                    left = j

                if j > right:
                    right = j

        print(f"T: B: L: R:", top, bottom, left, right)

        width_padding = int(self.image.width * self.content_padding)
        height_padding = int(self.image.height * self.content_padding)

        print(f"PH:%s PW:%s", height_padding, width_padding)

        top = top - height_padding if (top - height_padding) >= 0 else 0
        bottom = bottom + height_padding if (bottom + height_padding) < self.image.height else self.image.height
        left = left - width_padding if (left - width_padding) >= 0 else 0
        right = right + width_padding if (right + width_padding) < self.image.width else self.image.width

        print(f"T: B: L: R:", top, bottom, left, right)

        self.image = self.image.crop((left, top, right, bottom))

