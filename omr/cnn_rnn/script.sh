#!/bin/bash
inputImage=${1}
outputFolder=${2}
fname=$(basename "$inputImage" | cut -d. -f1)
python /code/standalone_inference_over_image.py --detection_inference_graph /code/model.pb --input_image $inputImage --detection_label_map /code/category_mapping.txt --output_image ${outputFolder}${fname}_annotated.jpg --output_result ${outputFolder}annotations.txt
