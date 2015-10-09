# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.model import Label2Vol

def test_Label2Vol_inputs():
    input_map = dict(annot_file=dict(argstr='--annot %s',
    copyfile=False,
    mandatory=True,
    requires=('subject_id', 'hemi'),
    xor=('label_file', 'annot_file', 'seg_file', 'aparc_aseg'),
    ),
    aparc_aseg=dict(argstr='--aparc+aseg',
    mandatory=True,
    xor=('label_file', 'annot_file', 'seg_file', 'aparc_aseg'),
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fill_thresh=dict(argstr='--fillthresh %.f',
    ),
    hemi=dict(argstr='--hemi %s',
    ),
    identity=dict(argstr='--identity',
    xor=('reg_file', 'reg_header', 'identity'),
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    invert_mtx=dict(argstr='--invertmtx',
    ),
    label_file=dict(argstr='--label %s...',
    copyfile=False,
    mandatory=True,
    xor=('label_file', 'annot_file', 'seg_file', 'aparc_aseg'),
    ),
    label_hit_file=dict(argstr='--hits %s',
    ),
    label_voxel_volume=dict(argstr='--labvoxvol %f',
    ),
    map_label_stat=dict(argstr='--label-stat %s',
    ),
    native_vox2ras=dict(argstr='--native-vox2ras',
    ),
    proj=dict(argstr='--proj %s %f %f %f',
    requires=('subject_id', 'hemi'),
    ),
    reg_file=dict(argstr='--reg %s',
    xor=('reg_file', 'reg_header', 'identity'),
    ),
    reg_header=dict(argstr='--regheader %s',
    xor=('reg_file', 'reg_header', 'identity'),
    ),
    seg_file=dict(argstr='--seg %s',
    copyfile=False,
    mandatory=True,
    xor=('label_file', 'annot_file', 'seg_file', 'aparc_aseg'),
    ),
    subject_id=dict(argstr='--subject %s',
    ),
    subjects_dir=dict(),
    surface=dict(argstr='--surf %s',
    ),
    template_file=dict(argstr='--temp %s',
    mandatory=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    vol_label_file=dict(argstr='--o %s',
    genfile=True,
    ),
    )
    inputs = Label2Vol.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Label2Vol_outputs():
    output_map = dict(vol_label_file=dict(),
    )
    outputs = Label2Vol.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

