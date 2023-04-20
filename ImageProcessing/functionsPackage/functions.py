# functions.py

from PIL import Image, ImageFilter, ImageDraw, ImageFont

'''
    Load an image file from disk
    :param filename: The file to load
    :return the image object
'''

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        # bad idea to have a print statement as function says it will load an image
        # the UI might be messed up by this 
        # print("Unable to open", filename) 
        '''
        Raise an exception instead
        '''
        raise Exception("Unable to open" + filename)
        return None  # not much else to do, could not load image still results in another error but we are not concerned with that error
    return myimage
