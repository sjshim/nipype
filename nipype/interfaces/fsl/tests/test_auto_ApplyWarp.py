# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import ApplyWarp

def test_ApplyWarp_inputs():
    input_map = dict(abswarp=dict(argstr='--abs',
    xor=['relwarp'],
    ),
    args=dict(argstr='%s',
    ),
    datatype=dict(argstr='--datatype=%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    field_file=dict(argstr='--warp=%s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='--in=%s',
    mandatory=True,
    position=0,
    ),
    interp=dict(argstr='--interp=%s',
    position=-2,
    ),
    mask_file=dict(argstr='--mask=%s',
    ),
    out_file=dict(argstr='--out=%s',
    genfile=True,
    hash_files=False,
    position=2,
    ),
    output_type=dict(),
    postmat=dict(argstr='--postmat=%s',
    ),
    premat=dict(argstr='--premat=%s',
    ),
    ref_file=dict(argstr='--ref=%s',
    mandatory=True,
    position=1,
    ),
    relwarp=dict(argstr='--rel',
    position=-1,
    xor=['abswarp'],
    ),
    superlevel=dict(argstr='--superlevel=%s',
    ),
    supersample=dict(argstr='--super',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = ApplyWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ApplyWarp_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = ApplyWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

