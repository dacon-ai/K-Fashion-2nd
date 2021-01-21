_base_ = '../htc/htc_r50_fpn_1x_coco.py'

model = dict(
    backbone=dict(
        type='DetectoRS_ResNet',
        conv_cfg=dict(type='ConvAWS'),
        sac=dict(type='SAC', use_deform=True),
        stage_with_sac=(False, True, True, True),
        output_img=True),
    neck=dict(
        type='RFP',
        rfp_steps=2,
        aspp_out_channels=64,
        aspp_dilations=(1, 3, 6, 1),
        rfp_backbone=dict(
            rfp_inplanes=256,
            type='DetectoRS_ResNet',
            depth=50,
            num_stages=4,
            out_indices=(0, 1, 2, 3),
            frozen_stages=1,
            norm_cfg=dict(type='BN', requires_grad=True),
            norm_eval=True,
            conv_cfg=dict(type='ConvAWS'),
            sac=dict(type='SAC', use_deform=True),
            stage_with_sac=(False, True, True, True),
            pretrained='torchvision://resnet50',
            style='pytorch')))


classes = ('top', 'blouse', 't-shirt', 'Knitted fabri', 'shirt', 'bra top',
           'hood', 'blue jeans', 'pants', 'skirt', 'leggings', 'jogger pants',
           'coat', 'jacket', 'jumper', 'padding jacket', 'best', 'kadigan',
           'zip up', 'dress', 'jumpsuit')

data = dict(train=dict(classes=classes), val=dict(classes=classes), test=dict(classes=classes))
# learning policy
lr_config = dict(step=[34, 42])
total_epochs = 48