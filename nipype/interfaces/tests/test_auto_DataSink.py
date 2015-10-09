# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.io import DataSink

def test_DataSink_inputs():
    input_map = dict(_outputs=dict(usedefault=True,
    ),
    base_directory=dict(),
    container=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    parameterization=dict(usedefault=True,
    ),
    regexp_substitutions=dict(),
    remove_dest_dir=dict(usedefault=True,
    ),
    strip_dir=dict(),
    substitutions=dict(),
    )
    inputs = DataSink.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DataSink_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = DataSink.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

