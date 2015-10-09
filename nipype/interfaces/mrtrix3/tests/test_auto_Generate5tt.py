# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix3.utils import Generate5tt

def test_Generate5tt_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_fast=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    in_first=dict(argstr='%s',
    position=-2,
    ),
    out_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Generate5tt.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Generate5tt_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Generate5tt.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

