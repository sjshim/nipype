# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.diffusion.gtract import compareTractInclusion

def test_compareTractInclusion_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    closeness=dict(argstr='--closeness %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    numberOfPoints=dict(argstr='--numberOfPoints %d',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    standardFiber=dict(argstr='--standardFiber %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    testFiber=dict(argstr='--testFiber %s',
    ),
    testForBijection=dict(argstr='--testForBijection ',
    ),
    testForFiberCardinality=dict(argstr='--testForFiberCardinality ',
    ),
    writeXMLPolyDataFile=dict(argstr='--writeXMLPolyDataFile ',
    ),
    )
    inputs = compareTractInclusion.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_compareTractInclusion_outputs():
    output_map = dict()
    outputs = compareTractInclusion.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

