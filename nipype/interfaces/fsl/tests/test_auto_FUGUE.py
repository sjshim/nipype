# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import FUGUE

def test_FUGUE_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    asym_se_time=dict(argstr='--asym=%.10f',
    ),
    despike_2dfilter=dict(argstr='--despike',
    ),
    despike_threshold=dict(argstr='--despikethreshold=%s',
    ),
    dwell_time=dict(argstr='--dwell=%.10f',
    ),
    dwell_to_asym_ratio=dict(argstr='--dwelltoasym=%.10f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fmap_in_file=dict(argstr='--loadfmap=%s',
    ),
    fmap_out_file=dict(argstr='--savefmap=%s',
    ),
    forward_warping=dict(usedefault=True,
    ),
    fourier_order=dict(argstr='--fourier=%d',
    ),
    icorr=dict(argstr='--icorr',
    requires=['shift_in_file'],
    ),
    icorr_only=dict(argstr='--icorronly',
    requires=['unwarped_file'],
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='--in=%s',
    ),
    mask_file=dict(argstr='--mask=%s',
    ),
    median_2dfilter=dict(argstr='--median',
    ),
    no_extend=dict(argstr='--noextend',
    ),
    no_gap_fill=dict(argstr='--nofill',
    ),
    nokspace=dict(argstr='--nokspace',
    ),
    output_type=dict(),
    pava=dict(argstr='--pava',
    ),
    phase_conjugate=dict(argstr='--phaseconj',
    ),
    phasemap_in_file=dict(argstr='--phasemap=%s',
    ),
    poly_order=dict(argstr='--poly=%d',
    ),
    save_fmap=dict(xor=['save_unmasked_fmap'],
    ),
    save_shift=dict(xor=['save_unmasked_shift'],
    ),
    save_unmasked_fmap=dict(argstr='--unmaskfmap',
    xor=['save_fmap'],
    ),
    save_unmasked_shift=dict(argstr='--unmaskshift',
    xor=['save_shift'],
    ),
    shift_in_file=dict(argstr='--loadshift=%s',
    ),
    shift_out_file=dict(argstr='--saveshift=%s',
    ),
    smooth2d=dict(argstr='--smooth2=%.2f',
    ),
    smooth3d=dict(argstr='--smooth3=%.2f',
    ),
    terminal_output=dict(nohash=True,
    ),
    unwarp_direction=dict(argstr='--unwarpdir=%s',
    ),
    unwarped_file=dict(argstr='--unwarp=%s',
    requires=['in_file'],
    xor=['warped_file'],
    ),
    warped_file=dict(argstr='--warp=%s',
    requires=['in_file'],
    xor=['unwarped_file'],
    ),
    )
    inputs = FUGUE.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_FUGUE_outputs():
    output_map = dict(fmap_out_file=dict(),
    shift_out_file=dict(),
    unwarped_file=dict(),
    warped_file=dict(),
    )
    outputs = FUGUE.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

