# TextPlusImage
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/workink/TextPlusImage/blob/master/LICENSE)

A tool to add texts to images is given in this repository. Users need to give `image_path`, `text`, `output_folder` as
the input. The output is an image saved in the `output_folder`, which combines the original image with the text.

## Installing
Activate the virtualenv and install packages using `requirements.txt`.
```bash
pip install -r requirements.txt
```

## Usage
Pass `--helpshort` to see help on flags.
```
python text_plus_image.py --helpshort

       USAGE: text_plus_image.py [flags]
flags:

text_plus_image.py:
  --image_path: The path of the image to process
  --output_folder: The output folder of the result
    (default: './text_plus_image_output')
  --text: The text to add to the image

Try --helpfull to get a list of all flags.
```

Sample usage.
```
python text_plus_image.py --image_path="./data/400_600.jpg" --text="mytext"
```
