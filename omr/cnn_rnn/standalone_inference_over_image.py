import argparse
import os

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image, ImageColor

if tf.__version__ < '1.4.0':
    raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')

STANDARD_COLORS = [
    'AliceBlue', 'Chartreuse', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque',
    'BlanchedAlmond', 'BlueViolet', 'BurlyWood', 'CadetBlue', 'AntiqueWhite',
    'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan',
    'DarkCyan', 'DarkGoldenRod', 'DarkGrey', 'DarkKhaki', 'DarkOrange',
    'DarkOrchid', 'DarkSalmon', 'DarkSeaGreen', 'DarkTurquoise', 'DarkViolet',
    'DeepPink', 'DeepSkyBlue', 'DodgerBlue', 'FireBrick', 'FloralWhite',
    'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod',
    'Salmon', 'Tan', 'HoneyDew', 'HotPink', 'IndianRed', 'Ivory', 'Khaki',
    'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue',
    'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey',
    'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue',
    'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime',
    'LimeGreen', 'Linen', 'Magenta', 'MediumAquaMarine', 'MediumOrchid',
    'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen',
    'MediumTurquoise', 'MediumVioletRed', 'MintCream', 'MistyRose', 'Moccasin',
    'NavajoWhite', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed',
    'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed',
    'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple',
    'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Green', 'SandyBrown',
    'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue',
    'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'GreenYellow',
    'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
    'WhiteSmoke', 'Yellow', 'YellowGreen'
]


def run_inference_for_single_image(image, graph):
    with graph.as_default():
        with tf.Session() as sess:
            ops = tf.get_default_graph().get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            tensor_dict = {}
            for key in [
                'num_detections',
                'detection_boxes',
                'detection_scores',
                'detection_classes'
            ]:
                tensor_name = key + ':0'

                if tensor_name in all_tensor_names:
                    tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)

            image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

            # Run inference
            output_dict = sess.run(tensor_dict, feed_dict={image_tensor: np.expand_dims(image, 0)})

            # all outputs are float32 numpy arrays, so convert types as appropriate
            output_dict['num_detections'] = int(output_dict['num_detections'][0])
            output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
            output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
            output_dict['detection_scores'] = output_dict['detection_scores'][0]

            return output_dict


def load_detection_graph(path_to_checkpoint):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(path_to_checkpoint, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    return detection_graph


def build_map(path_to_labelmap):
    int2category = {}
    lines = open(path_to_labelmap, 'r').read().splitlines()

    for line in lines:
        integer, category = line.split()
        int2category[int(integer)] = category

    return int2category


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Performs detection over input image given a trained detector.')
    parser.add_argument('--detection_inference_graph', type=str,
                        default="2018-05-15_faster-rcnn_inception-resnet-v2_2000-proposals_full-page-detection_muscima-pp.pb",
                        help='Path to the frozen inference graph.')
    parser.add_argument('--input_image', type=str, default="w-21_p008.png", help='Path to the input image.')
    parser.add_argument('--detection_label_map', type=str, default="category_mapping.txt",
                        help='Path to the label map, which maps each category name to a unique number.'
                             'Must be a simple text-file with one mapping per line in the form of:'
                             '"<number> <label>", e.g. "1 barline".')
    parser.add_argument('--output_image', type=str, default="annotated_image.jpg",
                        help='Path to the output image, with highlighted boxes.')
    parser.add_argument('--output_result', type=str, default="output_transcript.txt",
                        help='Path to the output file, that will contain a list of detection, '
                             'including position-classification')
    args = parser.parse_args()

    # Uncomment the next line on Windows to run the evaluation on the CPU
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    # Build category map
    detection_category_mapping = build_map(args.detection_label_map)
    class_to_index_mapping = {value: key for key, value in detection_category_mapping.items()}

    # Read frozen graphs
    detection_graph = load_detection_graph(args.detection_inference_graph)

    # PIL Image
    image = Image.open(args.input_image).convert("RGB")
    (image_width, image_height) = image.size

    # Opencv Image (draw)
    image_cv = cv2.imread(args.input_image, True)

    # Numpy image
    image_np = np.array(image.getdata()).reshape((image_height, image_width, 3)).astype(np.uint8)

    # Actual detection;
    output_dict = run_inference_for_single_image(image_np, detection_graph)
    output_lines = []

    for idx in range(output_dict['num_detections']):
        if output_dict['detection_scores'][idx] > 0.5:

            y1, x1, y2, x2 = output_dict['detection_boxes'][idx]

            y1 = y1 * image_height
            y2 = y2 * image_height
            x1 = x1 * image_width
            x2 = x2 * image_width
            detected_class = detection_category_mapping[output_dict['detection_classes'][idx]]

            output_line = "{0:.3f},{1:.3f},{2:.3f},{3:.3f};{4}".format(x1, y1, x2, y2, detected_class)
            print(output_line)
            output_lines.append(output_line)

            if args.output_image is not None:
                color_name = STANDARD_COLORS[class_to_index_mapping[detected_class] % len(STANDARD_COLORS)]
                color_rgb = ImageColor.getrgb(color_name)
                cv2.rectangle(image_cv, (int(x1), int(y1)), (int(x2), int(y2)), color_rgb, 3)

        else:
            break

    if args.output_image is not None:
        cv2.imwrite(args.output_image, image_cv)

    with open(args.output_result, "w") as output_file:
        output_file.write("\n".join(output_lines))
