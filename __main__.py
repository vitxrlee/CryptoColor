import sys
import modules
try: 
    import PIL
except ImportError:
    sys.exit(
        "PIL is not installed, please install it."
    )

if __name__=="__main__": 
    main = modules.Manager()
    main.run()
