from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import json
import cv2
import matplotlib.pyplot as plt
import numpy as np

pdf_data = {}

with open('data/result_json/one.json', 'w') as f:
    for page_layout in extract_pages('data/pdf_sample/one.pdf'):
        page_width = page_layout.bbox[2]
        page_height = page_layout.bbox[3]
        pdf_data['page_width'] = page_width
        pdf_data['page_height'] = page_height

        data_list = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                if len(element.get_text().strip()) > 0:
                    data_item = {}
                    data_item['text'] = element.get_text().strip()
                    data_item['bbox'] = {}
                    data_item['bbox']['x1'] = element.bbox[0]
                    data_item['bbox']['y1'] = element.bbox[1]
                    data_item['bbox']['x2'] = element.bbox[2]
                    data_item['bbox']['y2'] = element.bbox[3]
                    print("==> " + element.get_text().strip() + str(element.bbox))

                    data_list.append(data_item)

        pdf_data['data_list'] = data_list

        pdf_data_json = json.dumps(pdf_data)
        f.write(pdf_data_json)


def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros(
    (int(pdf_data['page_height']), int(pdf_data['page_width']), 3), dtype='uint8')

image[:] = colors['light_gray']

# print(data_list)
print(pdf_data['page_height'])
print(pdf_data['page_width'])

for i in data_list:
    cv2.rectangle(image, (int(i['bbox']['x1']), int(i['bbox']['y1'])), (int(
        i['bbox']['x2']), int(i['bbox']['y2'])), colors['blue'], 1)
    cv2.putText(image, i['text'], (int(i['bbox']['x1']), int(
        i['bbox']['y1'])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.4, colors['black'], 1, cv2.LINE_AA)

show_with_matplotlib(image, 'PDF data')
