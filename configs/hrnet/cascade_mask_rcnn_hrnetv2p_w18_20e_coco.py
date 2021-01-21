_base_ = './cascade_mask_rcnn_hrnetv2p_w32_20e_coco.py'
# model settings
model = dict(
    pretrained='open-mmlab://msra/hrnetv2_w18',
    backbone=dict(
        extra=dict(
            stage2=dict(num_channels=(18, 36)),
            stage3=dict(num_channels=(18, 36, 72)),
            stage4=dict(num_channels=(18, 36, 72, 144)))),
    neck=dict(type='HRFPN', in_channels=[18, 36, 72, 144], out_channels=256))


classes = ('top', 'blouse', 't-shirt', 'Knitted fabri', 'shirt', 'bra top',
           'hood', 'blue jeans', 'pants', 'skirt', 'leggings', 'jogger pants',
           'coat', 'jacket', 'jumper', 'padding jacket', 'best', 'kadigan',
           'zip up', 'dress', 'jumpsuit')


data = dict(train=dict(classes=classes), val=dict(classes=classes), test=dict(classes=classes))