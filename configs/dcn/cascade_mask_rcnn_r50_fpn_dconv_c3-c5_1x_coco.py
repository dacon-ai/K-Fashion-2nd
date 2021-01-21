_base_ = '../cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)))


classes = ('top', 'blouse', 't-shirt', 'Knitted fabri', 'shirt', 'bra top',
           'hood', 'blue jeans', 'pants', 'skirt', 'leggings', 'jogger pants',
           'coat', 'jacket', 'jumper', 'padding jacket', 'best', 'kadigan',
           'zip up', 'dress', 'jumpsuit')

data = dict(train=dict(classes=classes), val=dict(classes=classes), test=dict(classes=classes))