1. model prediction step
```
sh ./tools/dist_test.sh \
./configs/dcn/cascade_mask_rcnn_r50_fpn_dconv_c3-c5_1x_coco.py \
./work_dirs/cascade_mask_rcnn_r50_fpn_dconv_c3-c5_1x_coco/latest.pth \
4 \
--format-only \
--eval-options "jsonfile_prefix=results"
result:
 results.bbox.json
 results.segm.json
```

2. create a submit file
```
jupyter lab ./
all run: inference.ipynb
 result:
 last_text.csv -> submit file
```