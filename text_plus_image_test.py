import text_plus_image
import os

'''
Test cases:

image_size              text_word_number
40 x 40                 1
60 x 400                2
400 x 600        *      5
600 x 40                10
600 x 400               100
'''

image = ["40_40.jpg", "60_400.jpg", "400_600.jpg", "600_40.jpg", "600_400.jpg"]
text = ['cat', 'cat dog', 'cat dog bird monkey lion', 'cat dog bird monkey lion ' * 20]

for img in image:
    image_path = '../data/' + img
    output_folder = './text_plus_image_output'
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError:
            raise
    for txt in text:
        text_plus_image.text_plus_image(image_path, txt)
