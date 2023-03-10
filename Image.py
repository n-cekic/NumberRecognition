from PIL import Image, ImageOps


class ImagePreprocessing:
    def __init__(self, path=None):
        self.image = None

        if path is not None:
            self.open(path)

        self.new_width = 8
        self.new_height = 8
        self.cutoff = 110
        self.content_padding = 0.01

    def open(self, path):
        self.image = Image.open(path)

    def pixelate(self):
        self.image = self.image.resize((self.new_width, self.new_height))

    def to_gray(self):
        self.image = self.image.convert("L")

    def invert(self):
        self.image = ImageOps.invert(self.image)

    def locate_content(self):
        top = 9999
        left = 9999
        right = -1
        bottom = -1
        for i in range(0, self.image.height):
            for j in range(0, self.image.width):
                if self.image.getpixel((j, i)) > self.cutoff:
                    continue
                if i < top:
                    top = i

                if i > bottom:
                    bottom = i

                if j < left:
                    left = j

                if j > right:
                    right = j

        width_padding = int(self.image.width * self.content_padding)
        height_padding = int(self.image.height * self.content_padding)

        top = top - height_padding if (top - height_padding) >= 0 else 0
        bottom = bottom + height_padding if (bottom + height_padding) < self.image.height else self.image.height
        left = left - width_padding if (left - width_padding) >= 0 else 0
        right = right + width_padding if (right + width_padding) < self.image.width else self.image.width

        self.image = self.image.crop((left, top, right, bottom))

