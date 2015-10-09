# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.utilities.brains import ImageRegionPlotter

def test_ImageRegionPlotter_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputBinaryROIVolume=dict(argstr='--inputBinaryROIVolume %s',
    ),
    inputLabelVolume=dict(argstr='--inputLabelVolume %s',
    ),
    inputVolume1=dict(argstr='--inputVolume1 %s',
    ),
    inputVolume2=dict(argstr='--inputVolume2 %s',
    ),
    numberOfHistogramBins=dict(argstr='--numberOfHistogramBins %d',
    ),
    outputJointHistogramData=dict(argstr='--outputJointHistogramData %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    useIntensityForHistogram=dict(argstr='--useIntensityForHistogram ',
    ),
    useROIAUTO=dict(argstr='--useROIAUTO ',
    ),
    verbose=dict(argstr='--verbose ',
    ),
    )
    inputs = ImageRegionPlotter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ImageRegionPlotter_outputs():
    output_map = dict()
    outputs = ImageRegionPlotter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

