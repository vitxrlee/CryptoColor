<h1>CryptoColor <img src=demo/anaconda_final.png width=20></img></h1>

[![python](https://img.shields.io/badge/python->=3.7-blue.svg)](https://www.python.org) [![repo size](https://img.shields.io/github/repo-size/vlHan/CryptoColor)](#) [![build](https://img.shields.io/badge/build-Passing-green)](#) [![license](https://img.shields.io/github/license/vlHan/CryptoColor.svg)](LICENSE)

RGB Cryptography, which read the bytes from a file and transform this file in RGB list (similar with spectro).

## How it works 
- Encoder - transform file to an image (png)
- Decoder - transform the image (png) generated to the initial file 

### Anaconda application
<img src=demo/anaconda.png width=200></img>

### 1) File to numbers
Transform the inputed file into a byte array:
```
[34, 234, 67, 8, 45, 23, 253, 124, 32]
```

### 2) Numbers to colors
- Put the numbers from the byte array into a rgb code list made with tuples:
```
(34, 234, 67) (8, 45, 23) (253, 124, 32)
```
### 3) Colors to images
- Export the rgb code list into a image.
- Complete the final pixels with (255, 255, 255) to make a square:
```py
color_edge.append(
    (self.byte[color_position], 256, 256)
)
```
### Final image
<img src=demo/anaconda_final.png width=200></img>

## Contributors
See also the list of contributors who participated in this project.

- **[vlHan](https://github.com/vlHan)** - *Idea (Initial work)*

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

## License 
This project is licensed under the MIT License, see the [LICENSE](https://github.com/vlHan/CryptoColor/blob/master/LICENSE) file for details
