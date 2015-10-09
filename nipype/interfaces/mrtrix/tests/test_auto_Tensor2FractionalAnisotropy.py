# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix.preprocess import Tensor2FractionalAnisotropy

def test_Tensor2FractionalAnisotropy_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    debug=dict(argstr='-debug',
    position=1,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    out_filename=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    quiet=dict(argstr='-quiet',
    position=1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Tensor2FractionalAnisotropy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Tensor2FractionalAnisotropy_outputs():
    output_map = dict(FA=dict(),
    )
    outputs = Tensor2FractionalAnisotropy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

