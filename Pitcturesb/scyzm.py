# from captcha.image import ImageCaptcha
# from PIL import Image
# text='5690'
# image=ImageCaptcha()
# captcha=image.generate(text)
# captcha_image=Image.open(captcha)
# captcha_image.show()

from PIL import Image
from captcha.image import ImageCaptcha
import numpy as np
VOCAB = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','Z','T','L']
CAPTCHA_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)
def generate_captcha(captcha_text):

    image = ImageCaptcha()
    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_array = np.array(captcha_image)
    return captcha_array



def text2vec(text):
    """
    text to one-hot vector
    :param text: source text
    :return: np array
    """

    if len(text) > CAPTCHA_LENGTH:
        return False
    vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
    for i, c in enumerate(text):
        index = i * VOCAB_LENGTH + VOCAB.index(c)
        vector[index] = 1
    return vector


def vec2text(vector):
    """
    vector to captcha text
    :param vector: np array
    :return: text
    """
    if not isinstance(vector, np.ndarray):
        vector = np.asarray(vector)
    vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])
    text = ''
    for item in vector:
        text += VOCAB[np.argmax(item)]
    return text
vector = text2vec('Z2TL')
text = vec2text(vector)
print(vector, text)

