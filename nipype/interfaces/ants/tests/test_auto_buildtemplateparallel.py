# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.ants.legacy import buildtemplateparallel

def test_buildtemplateparallel_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bias_field_correction=dict(argstr='-n 1',
    ),
    dimension=dict(argstr='-d %d',
    position=1,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    gradient_step_size=dict(argstr='-g %f',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_files=dict(argstr='%s',
    mandatory=True,
    position=-1,
    ),
    iteration_limit=dict(argstr='-i %d',
    usedefault=True,
    ),
    max_iterations=dict(argstr='-m %s',
    sep='x',
    ),
    num_cores=dict(argstr='-j %d',
    requires=['parallelization'],
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    out_prefix=dict(argstr='-o %s',
    usedefault=True,
    ),
    parallelization=dict(argstr='-c %d',
    usedefault=True,
    ),
    rigid_body_registration=dict(argstr='-r 1',
    ),
    similarity_metric=dict(argstr='-s %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    transformation_model=dict(argstr='-t %s',
    usedefault=True,
    ),
    use_first_as_target=dict(),
    )
    inputs = buildtemplateparallel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_buildtemplateparallel_outputs():
    output_map = dict(final_template_file=dict(),
    subject_outfiles=dict(),
    template_files=dict(),
    )
    outputs = buildtemplateparallel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

