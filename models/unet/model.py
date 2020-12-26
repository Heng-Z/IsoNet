from mwr.models.unet import builder,builder_fullconv,builder_fullconv_old

def Unet(filter_base=32,
        depth=2,
        convs_per_depth=2,
        kernel=(3,3),
        batch_norm=False,
        dropout=0.0,
        pool=(2,2)):

    # model = builder.build_unet(filter_base,depth,convs_per_depth,
    #            kernel,
    #            batch_norm,
    #            dropout,
    #            pool)
#     model = builder_fullconv.build_unet(filter_base,depth,convs_per_depth,
#             kernel,
#             batch_norm,
#             dropout,
#             pool)
    import os
    import sys
    cwd = os.getcwd()
    sys.path.insert(0,cwd)
    import train_settings 
    model = builder_fullconv_old.build_unet(train_settings)
    return model