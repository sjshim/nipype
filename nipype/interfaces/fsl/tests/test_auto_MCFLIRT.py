# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import MCFLIRT

def test_MCFLIRT_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bins=dict(argstr='-bins %d',
    ),
    cost=dict(argstr='-cost %s',
    ),
    dof=dict(argstr='-dof %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-in %s',
    mandatory=True,
    position=0,
    ),
    init=dict(argstr='-init %s',
    ),
    interpolation=dict(argstr='-%s_final',
    ),
    mean_vol=dict(argstr='-meanvol',
    ),
    out_file=dict(argstr='-out %s',
    genfile=True,
    hash_files=False,
    ),
    output_type=dict(),
    ref_file=dict(argstr='-reffile %s',
    ),
    ref_vol=dict(argstr='-refvol %d',
    ),
    rotation=dict(argstr='-rotation %d',
    ),
    save_mats=dict(argstr='-mats',
    ),
    save_plots=dict(argstr='-plots',
    ),
    save_rms=dict(argstr='-rmsabs -rmsrel',
    ),
    scaling=dict(argstr='-scaling %.2f',
    ),
    smooth=dict(argstr='-smooth %.2f',
    ),
    stages=dict(argstr='-stages %d',
    ),
    stats_imgs=dict(argstr='-stats',
    ),
    terminal_output=dict(nohash=True,
    ),
    use_contour=dict(argstr='-edge',
    ),
    use_gradient=dict(argstr='-gdt',
    ),
    )
    inputs = MCFLIRT.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_MCFLIRT_outputs():
    output_map = dict(mat_file=dict(),
    mean_img=dict(),
    out_file=dict(),
    par_file=dict(),
    rms_files=dict(),
    std_img=dict(),
    variance_img=dict(),
    )
    outputs = MCFLIRT.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

