# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.elastix.registration import PointsWarp

def test_PointsWarp_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    num_threads=dict(argstr='-threads %01d',
    nohash=True,
    ),
    output_path=dict(argstr='-out %s',
    mandatory=True,
    usedefault=True,
    ),
    points_file=dict(argstr='-def %s',
    mandatory=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    transform_file=dict(argstr='-tp %s',
    mandatory=True,
    ),
    )
    inputs = PointsWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_PointsWarp_outputs():
    output_map = dict(warped_file=dict(),
    )
    outputs = PointsWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

