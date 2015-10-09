# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.diffusion.gtract import gtractAnisotropyMap

def test_gtractAnisotropyMap_inputs():
    input_map = dict(anisotropyType=dict(argstr='--anisotropyType %s',
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputTensorVolume=dict(argstr='--inputTensorVolume %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = gtractAnisotropyMap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_gtractAnisotropyMap_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = gtractAnisotropyMap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

