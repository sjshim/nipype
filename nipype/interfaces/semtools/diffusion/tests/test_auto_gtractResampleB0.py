# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.diffusion.gtract import gtractResampleB0

def test_gtractResampleB0_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputAnatomicalVolume=dict(argstr='--inputAnatomicalVolume %s',
    ),
    inputTransform=dict(argstr='--inputTransform %s',
    ),
    inputVolume=dict(argstr='--inputVolume %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    transformType=dict(argstr='--transformType %s',
    ),
    vectorIndex=dict(argstr='--vectorIndex %d',
    ),
    )
    inputs = gtractResampleB0.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_gtractResampleB0_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = gtractResampleB0.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

