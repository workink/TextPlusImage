from PIL import Image, ImageDraw, ImageFont
from absl import flags
from absl import app
import textwrap
import os

FLAGS = flags.FLAGS

flags.DEFINE_string('image_path', None, 'The path of the image to process')
flags.DEFINE_string('text', None, 'The text to add to the image')
flags.DEFINE_string('output_folder', './text_plus_image_output', 'The output folder of the result')
flags.mark_flag_as_required('image_path')
flags.mark_flag_as_required('text')

default_word_num = 20
valid_images = [".jpg", ".png"]


def text_plus_image(image_path, text, font_size=15, output_folder='./text_plus_image_output'):
    saved_img_name = ''.join([os.path.splitext(os.path.basename(image_path))[0], '_plus_text',
                              os.path.splitext(os.path.basename(image_path))[1]])
    img = Image.open(image_path)
    img_width, img_height = img.size
    text_length = len(text)

    min_length = font_size * default_word_num
    min_length = min_length if min_length < text_length * font_size else (text_length * font_size)

    longer_length = img_height if img_height > img_width else img_width
    longer_length = longer_length if longer_length > min_length else min_length

    another_length = text_length * font_size * font_size // longer_length + font_size * 5
    another_length = another_length if another_length > min_length else min_length

    text_img = Image.new('RGB',
                         (another_length, longer_length) if img_width < img_height else (longer_length, another_length),
                         color='white')
    draw = ImageDraw.Draw(text_img)
    font = ImageFont.truetype("arial.ttf", font_size)

    text_img_width, text_img_height = text_img.size

    lines = textwrap.wrap(text, width=text_img_width // (font_size - 3))
    y_text = 0
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((text_img_width - line_width) / 2, y_text),
                  line, font=font, fill='black')
        y_text += line_height

    if img_width > img_height:
        concat_img = Image.new('RGB', (max(img_width, text_img_width), img_height + text_img_height), color='white')
        concat_img.paste(img, (0, 0))
        concat_img.paste(text_img, (0, img_height))
        concat_img.save(os.path.join(output_folder, saved_img_name))
    else:
        concat_img = Image.new('RGB', (img_width + text_img_width, max(img_height, text_img_height)), color='white')
        concat_img.paste(img, (0, 0))
        concat_img.paste(text_img, (img_width, 0))
        concat_img.save(os.path.join(output_folder, saved_img_name))
    return


def main(unused_argv):
    image_path = FLAGS.image_path
    text = FLAGS.text
    output_folder = FLAGS.output_folder

    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError:
            raise

    if os.path.isfile(image_path):
        text_plus_image(image_path, text, output_folder=output_folder)
    elif os.path.isdir(image_path):
        for f in os.listdir(image_path):
            ext = os.path.splitext(f)[1]
            if ext.lower() in valid_images:
                text_plus_image(os.path.join(image_path, f), text, output_folder=output_folder)
    else:
        print('this not a valid image path')


if __name__ == '__main__':
    app.run(main)
