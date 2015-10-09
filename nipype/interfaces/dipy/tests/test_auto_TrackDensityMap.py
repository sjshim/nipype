# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dipy.tracks import TrackDensityMap

def test_TrackDensityMap_inputs():
    input_map = dict(data_dims=dict(),
    in_file=dict(mandatory=True,
    ),
    out_filename=dict(usedefault=True,
    ),
    points_space=dict(usedefault=True,
    ),
    reference=dict(),
    voxel_dims=dict(),
    )
    inputs = TrackDensityMap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_TrackDensityMap_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = TrackDensityMap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

