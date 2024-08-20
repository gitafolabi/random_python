from rembg import remove
from PIL import Image
input_path = 'afolabi_omo.jpg'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input) 
output.save(output_path)
Image = Image.open(output_path)
Image.show()
Image.close()