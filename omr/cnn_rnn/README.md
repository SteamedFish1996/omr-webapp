# Running this demo

Download the trained model from 
- [2018-05-15_faster-rcnn_inception-resnet-v2_2000-proposals_full-page-detection_muscima-pp.pb](https://owncloud.tuwien.ac.at/index.php/s/5J1c8yhnVXB6Sm2/download)

and put it into the demo directory.

Then run `standalone_inference_over_image.py` from inside the demo directory:

```bash
python standalone_inference_over_image.py \
    --detection_inference_graph 2018-05-15_faster-rcnn_inception-resnet-v2_2000-proposals_full-page-detection_muscima-pp.pb \
    --input_image w-21_p008.png \
    --detection_label_map category_mapping.txt \
    --output_image annotated_image.jpg \
    --output_result output_transcript.txt
```

Note that the depicted parameters are the default-parameter, so if you are happy with them, they can be omitted (e.g. the label_maps).