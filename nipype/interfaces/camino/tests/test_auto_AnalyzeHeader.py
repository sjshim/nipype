# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.convert import AnalyzeHeader

def test_AnalyzeHeader_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    centre=dict(argstr='-centre %s',
    units='mm',
    ),
    data_dims=dict(argstr='-datadims %s',
    units='voxels',
    ),
    datatype=dict(argstr='-datatype %s',
    mandatory=True,
    ),
    description=dict(argstr='-description %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    greylevels=dict(argstr='-gl %s',
    units='NA',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='< %s',
    mandatory=True,
    position=1,
    ),
    initfromheader=dict(argstr='-initfromheader %s',
    position=3,
    ),
    intelbyteorder=dict(argstr='-intelbyteorder',
    ),
    networkbyteorder=dict(argstr='-networkbyteorder',
    ),
    nimages=dict(argstr='-nimages %d',
    units='NA',
    ),
    offset=dict(argstr='-offset %d',
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    picoseed=dict(argstr='-picoseed %s',
    units='mm',
    ),
    printbigendian=dict(argstr='-printbigendian %s',
    position=3,
    ),
    printimagedims=dict(argstr='-printimagedims %s',
    position=3,
    ),
    printintelbyteorder=dict(argstr='-printintelbyteorder %s',
    position=3,
    ),
    printprogargs=dict(argstr='-printprogargs %s',
    position=3,
    ),
    readheader=dict(argstr='-readheader %s',
    position=3,
    ),
    scaleinter=dict(argstr='-scaleinter %d',
    units='NA',
    ),
    scaleslope=dict(argstr='-scaleslope %d',
    units='NA',
    ),
    scheme_file=dict(argstr='%s',
    position=2,
    ),
    terminal_output=dict(nohash=True,
    ),
    voxel_dims=dict(argstr='-voxeldims %s',
    units='mm',
    ),
    )
    inputs = AnalyzeHeader.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_AnalyzeHeader_outputs():
    output_map = dict(header=dict(),
    )
    outputs = AnalyzeHeader.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

