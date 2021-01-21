_base_ = '../cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://msra/hrnetv2_w32',
    backbone=dict(
        _delete_=True,
        type='HRNet',
        extra=dict(
            stage1=dict(
                num_modules=1,
                num_branches=1,
                block='BOTTLENECK',
                num_blocks=(4, ),
                num_channels=(64, )),
            stage2=dict(
                num_modules=1,
                num_branches=2,
                block='BASIC',
                num_blocks=(4, 4),
                num_channels=(32, 64)),
            stage3=dict(
                num_modules=4,
                num_branches=3,
                block='BASIC',
                num_blocks=(4, 4, 4),
                num_channels=(32, 64, 128)),
            stage4=dict(
                num_modules=3,
                num_branches=4,
                block='BASIC',
                num_blocks=(4, 4, 4, 4),
                num_channels=(32, 64, 128, 256)))),
    neck=dict(
        _delete_=True,
        type='HRFPN',
        in_channels=[32, 64, 128, 256],
        out_channels=256))
# learning policy

classes = ('top', 'blouse', 't-shirt', 'Knitted fabri', 'shirt', 'bra top',
           'hood', 'blue jeans', 'pants', 'skirt', 'leggings', 'jogger pants',
           'coat', 'jacket', 'jumper', 'padding jacket', 'best', 'kadigan',
           'zip up', 'dress', 'jumpsuit')


data = dict(train=dict(classes=classes), val=dict(classes=classes), test=dict(classes=classes))


lr_config = dict(step=[16, 19])
total_epochs = 24
