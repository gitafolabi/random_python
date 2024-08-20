from captcha.image import ImageCaptcha
from PIL import Image

def gen_captcha_text(length):
    import string
    import random
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def gen_captcha(captcha_length=7, save_path='CAPTCHA.png'):
    image = ImageCaptcha(width=7000, height=100)
    captcha_text = gen_captcha_text(captcha_length)
    data = image.generate(captcha_text)
    image.write(captcha_text, save_path)
    return captcha_text

if __name__ == "__main__":
    captcha_text = gen_captcha()
    print(f"Generated CAPTCHA: {captcha_text}")
Image.open('CAPTCHA.png').show()