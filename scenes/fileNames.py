'''

File names and other parameters for pneunet and object files.
Dictionary elements correspond to specified value of "fea_variant" variable in scene file.
(used by singleFinger_wObject*.pyscn, singleFinger_wObject*.scn)

Note: filepaths are currently absolute, not relative. Edit dictionary elements as necessary.

'''


#########################
''' FEA/Pneunet files '''
#########################

''' store mass, file names based on FEA variant chosen '''
def fea_variant_mass (fea_variant):
    variantMasses = {
        'parab_ang_Ch0.2': 0.00337,
        'rect_ang_Ch0.2': 0.00251,
    } # note: masses in kg (current values assume SWX, silicone rubber ~5 MPa)
    return variantMasses.get(fea_variant, 0.001)    # return second arg if fea_variant not found


def fea_variant_STL (fea_variant):
    variantSTL_names = {
        'parab_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh_gmsh.stl',
        'rect_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_2mmmesh_gmsh.stl',
    }
    return variantSTL_names.get(fea_variant, 'FEA STL not found')    # return second arg if fea_variant not found

def fea_variant_VTK (fea_variant):
    variantVTK_names = {
        'parab_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh.vtk',
        'rect_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_2mmmesh.vtk',
    }
    return variantVTK_names.get(fea_variant, 'FEA VTK not found')    # return second arg if fea_variant not found

def fea_variant_airSTL (fea_variant):
    variantAirSTL_names = {
        'parab_ang_Ch0.2': 'Parab_FEA_4by41_Air_r1mm_gmsh.stl',
        'rect_ang_Ch0.2': 'new cavities/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_mesh3mm_gmsh.stl',#'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_2mmmesh_Air_gmsh.stl',
    }
    return variantAirSTL_names.get(fea_variant, 'FEA Air STL not found')    # return second arg if fea_variant not found

def stiffLayerCoords (fea_variant):
    stiffLayerCoords_names = {
        'parab_ang_Ch0.2':    '50 -14.2 5 50 -13.2 5 0 0.2 5 15', # thick: '50 -13.2 5 50 -12.2 5 0 1.2 5 15'
        'rect_ang_Ch0.2':     '50 -14.2 5 50 -13.2 5 0 0.2 5 15',
    }
    return stiffLayerCoords_names.get(fea_variant, '0 0 0 0 0 0')


def baseConstraint (fea_variant):
    variantBaseConstraint_names = {
        'parab_ang_Ch0.2': '3 -5 5 6 9 5 -2 10 5 15',
        'rect_ang_Ch0.2': '3 -5 5 6 9 5 -2 10 5 15',
    }
    return variantBaseConstraint_names.get(fea_variant, '0 0 0 0 0 0')


def fea_variant_cavity_placement (fea_variant):
    cavity_placements = {
        'parab_ang_Ch0.2':      ['47.38 -6.955 9.945', '90 180 -15'],
        'rect_ang_Ch0.2':      ['6.51 -1.64 0.65', '0 0 -15'], #['6.51 -1.64 1', '0 0 -15'],
    } # translations in mm, rotations in deg
    return cavity_placements.get(fea_variant, ['0 0 0', '0 0 0'])    # return second arg if fea_variant not found


def fea_variant_probe_indices (fea_variant):
    probeIndices_names = {
        'parab_ang_Ch0.2': '1537 1272 1576 1596 1618   1536 1008 1027 1049 1651  1527 1802 1795',# 1805 1799 1792 1855', #with r5mm cavity: '3099 2783',#'485 503 578 556 544',
        'rect_ang_Ch0.2': '613 616 540 587 575',
    }
    return probeIndices_names.get(fea_variant, '0 0 0 0 0')




####################
''' Object Files '''
####################

def obj_variant_STL (obj_variant):
    objSTLs = {
        'cyl_d50':   '...',
        'cyl_d100':  'cyl_d100_r10mm_gmsh.stl', # r3, r10 (use r10 for speed)
        'cyl_d200':  'cyl_d200_r15mm_gmsh.stl',
    }
    return objSTLs.get(obj_variant, '(Object STL not found)')

def obj_variant_VTK (obj_variant):
    objVTKs = {
        'cyl_d50':   '...',
        'cyl_d100':  'cyl_d100_r10mm.vtk', # r3, r10
        'cyl_d200':  'cyl_d200_r15mm.vtk',
    }
    return objVTKs.get(obj_variant, '(Object VTK not found)')

# note: offset due to suction disc radius currently hard-coded in (i.e. x position decreased by suction disc radius)
def obj_variant_position(obj_variant):
    obj_positions = {
        'cyl_d50':   ['0 0 0', '0 0 0'],
        'cyl_d100':  ['-63 1 -7.5', '90 0 0'], # y=1.75 for lower, soft
                # ('-63 0 -7.5' potentially fine; moving y up by 1 does not significantly change graph);
                # '-50 -2.5 -7.5' for centered orientation
        'cyl_d200':  ['-113 -2.5 -7.5', '90 0 0'], # '-100 -3 -7.5'
    } # first element: translation (x y z, mm), second element: rotation (x y z, deg)
    return obj_positions.get(obj_variant, ['0 0 0', '0 0 0'])

def obj_constraint (obj_variant):
    obj_boxROI = {
        'cyl_d50':  '...',
        'cyl_d100': '-70 -100 -15 40 -80 25', # ymax: -60 for higher, -80 for lower
        'cyl_d200': '-120 -210 -15 105 -160 25',
    } # boxROI coords: 'xmin ymin zmin xmax ymax zmax'
    return obj_boxROI.get(obj_variant, '0 0 0 0 0 0')

def obj_addConstraint (obj_variant):
    obj_boxROI = {
        'cyl_d50':  '...',
        'cyl_d100': '-70 -80 -15 -25 0 25',
        'cyl_d200': '-70 -100 -15 -25 0 25',
    } # boxROI coords: 'xmin ymin zmin xmax ymax zmax'
    return obj_boxROI.get(obj_variant, '0 0 0 0 0 0')

def obj_probeIndices (obj_variant):
    obj_indices = {
        'cyl_d50':  '0',
        'cyl_d100': '137 130 122 115 107', # r10mm
        'cyl_d200': '198 192 186 179 173 167', # r15mm, base: 204
    }
    return obj_indices.get(obj_variant, '0 0 0 0 0')

