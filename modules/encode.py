from PIL import Image
import math

import numpy


class Encode:
    """
    Extract data from files and encode them to RGB.
    """
    
    def __init__(self, filename):
        """
        filename = [str] 
        """
        self.filename = filename

    def read_file(self):
        """
        Read bytes from a file 
        """
        with open(self.filename, "rb") as f:
            return f.read()

    def transform_rgb(self):
        """
        Transform byte array into a RGB code list 
        """
        self.byte = self.read_file()

        byte_sqrt = int(math.sqrt(len(self.byte)/3))
        color = [] 
        color_position = 0 

        for _ in range(byte_sqrt):
            color_edge = []
            for _ in range(byte_sqrt):
                byte_length = len(self.byte)
                if (byte_length - 3) > color_position:
                    color_edge.append(
                        (self.byte[color_position], self.byte[color_position + 1], self.byte[color_position + 2])
                    )
                    color_position += 3

                elif (byte_length - 2) == color_position: 
                    color_edge.append(
                        (self.byte[color_position], self.byte[color_position + 1], 255)
                    )
                    color_position += 2

                elif (byte_length - 1) == color_position:
                    color_edge.append(
                        (self.byte[color_position], 256, 256)
                    )
                    color_position += 1
                    
                else: 
                    color_edge.append((256, 256, 256))

            color.append(color_edge)

        return numpy.array(color, dtype=numpy.uint8)

    def save_image(self):
        """
        Save the code list as an image
        """
        array = self.transform_rgb()

        new_img = Image.fromarray(array)
        new_img.save(f'{self.filename}.png')
