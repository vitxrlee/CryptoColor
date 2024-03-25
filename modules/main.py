from modules import *

class Manager:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        """
        Main function
        """
        file = str(input("[CryptoColor] Enter the file name: ")).strip()
        mode = str(input("[CryptoColor] Enter the mode (encode/decode): ")).strip()
        
        if mode == "encode":
            Encode(file).save_image()
            print("[CryptoColor] File Encrypted!")
        
        elif mode == "decode":
            if file.endswith(".png"):
                Decode(file).transform_byte()
                print("[CryptoColor] File Decrypted!")
            
            else:
                print("[CryptoColor] Invalid file type!")
