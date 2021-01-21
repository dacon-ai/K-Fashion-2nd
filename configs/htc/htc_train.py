_base_ = './htc_without_semantic_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnext101_64x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch',
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)))

classes = ('top', 'blouse', 't-shirt', 'Knitted fabri', 'shirt', 'bra top',
           'hood', 'blue jeans', 'pants', 'skirt', 'leggings', 'jogger pants',
           'coat', 'jacket', 'jumper', 'padding jacket', 'best', 'kadigan',
           'zip up', 'dress', 'jumpsuit')

data = dict(train=dict(classes=classes), val=dict(classes=classes), test=dict(classes=classes))
# learning policy
lr_config = dict(step=[34, 42])
total_epochs = 48
