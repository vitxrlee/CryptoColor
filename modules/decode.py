from PIL import Image


class Decode:
    """
    Decode data from RGB.

    If you have any error, please report at: https://github.com/vlHan/CryptoColor/issues
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read_image(self): 
        """
        Read the encrypted image 
        """
        img = Image.open(self.filename)
        return img.convert("RGB")

    def sizes_image(self): 
        """
        Get the sizes of the image 
        """
        img = self.read_image()
        return img.size

    def transform_byte(self):
        """
        Transform RGB code list into a byte array 
        """
        file_data = []

        width, height = self.sizes_image()

        for i in range(width):
            for j in range(height):
                pixel = self.read_image().getpixel((j, i))

                if pixel[0] != 256:
                    file_data.append(pixel[0])

                if pixel[1] != 256:
                    file_data.append(pixel[1])

                if pixel[2] != 256:
                    file_data.append(pixel[2])

        with open(self.filename[:len(self.filename) - 4], "wb") as f:
            f.write(bytearray(file_data))
