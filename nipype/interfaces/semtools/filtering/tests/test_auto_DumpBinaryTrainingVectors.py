# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.filtering.featuredetection import DumpBinaryTrainingVectors

def test_DumpBinaryTrainingVectors_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputHeaderFilename=dict(argstr='--inputHeaderFilename %s',
    ),
    inputVectorFilename=dict(argstr='--inputVectorFilename %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = DumpBinaryTrainingVectors.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DumpBinaryTrainingVectors_outputs():
    output_map = dict()
    outputs = DumpBinaryTrainingVectors.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

