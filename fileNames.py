'''

File names and other parameters for pneunet and object files
(used by singleFinger_wObject*.pyscn, singleFinger_wObject*.scn)

Note: filepaths are currently absolute, not relative. Edit dictionary elements as necessary.

'''


#########################
''' FEA/Pneunet files '''
#########################

''' store mass, file names based on FEA variant chosen '''
def fea_variant_mass (fea_variant):
    variantMasses = {
        'parab':     0.00337,
        'parab_ang': 0.00337,
        'parab_ang_comp': 0.00337,
        'parab_ang_SC': 0.00337,
        'parab_ang_SC_crs': 0.00337,
        'parab_ang_Ch0.2': 0.00337,
        'parab_ang_Ch0.2_crs': 0.00337,
        'parab_ang_Ch0.2_fine': 0.00337,
        'parab_4x41x11':            0.00337,
        'parab_4x41x11_Ch0.1_tall': 0.00337,    
        'parab_4x41x11_Ch0.1_tall_15deg': 0.00337,    
        'parab_4x41x11_Ch0.5':      0.00337,    # technically should be a bit higher bc SL layer
        'parab_4x41x11_Ch0.5_thin': 0.00337,    # technically should be a bit higher bc SL layer
        'parab_4x41x11_Ch0.5_tall': 0.00337,    # technically should be a bit higher
        'parab_4x41x11_Ch1.0':      0.00337,    # technically should be a bit higher bc SL layer
        'parab_4x41x20': 0.00658,
        'parab_9x41x20': 0.00932,
        'rect':     0.00251,
        'rect_ang': 0.00251,
        'rect_ang_comp': 0.00251,
        'rect_4x41x11':            0.00251,
        'rect_4x41x11_Ch0.1_tall': 0.00251,
        'rect_4x41x11_Ch0.1_tall_15deg': 0.00251, 
        'rect_4x41x11_Ch0.5':      0.00251,    # technically should be a bit higher bc SL layer
        'rect_4x41x11_Ch0.5_thin': 0.00251,    # technically should be a bit higher bc SL layer
        'rect_4x41x11_Ch0.5_tall': 0.00251,    # technically should be higher
        'rect_4x41x11_Ch1.0':      0.00251,    # technically should be a bit higher bc SL layer
        'rect_4x41x20': 0.00434,
        'rect_9x41x20': 0.00616,
        'rect_ang_Ch0.2': 0.00251,
        'rect_ang_Ch0.2_crs': 0.00251,
    } # note: masses in kg (current values assume SWX, silicone rubber ~5 MPa)
    return variantMasses.get(fea_variant, 0.001)    # return second arg if fea_variant not found


def fea_variant_STL (fea_variant):
    variantSTL_names = {
        'parab_4x41x11':            'Parab_FEA_4by41_11wide_r5mm_gmsh.stl',
        'parab_4x41x11_Ch0.1_tall': 'chamfer/new chamfers/15 deg/Parab_FEA_4by41_11wide_with_support_0.1mm_gmsh.stl',   
        'parab_4x41x11_Ch0.1_tall_15deg': 'chamfer/new chamfers/15 deg/Parab_FEA_4by41_11wide_with_support_15degAngle_0.1mm_gmsh.stl',
        'parab_4x41x11_Ch0.5':      'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_0.5mmchamfer_gmsh.stl',
        'parab_4x41x11_Ch0.5_thin': 'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_gmsh.stl',
        'parab_4x41x11_Ch0.5_tall': 'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_TALLER_gmsh.stl',
        'parab_4x41x11_Ch1.0':      'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_1mmchamfer_gmsh.stl',
        'parab_4x41x20':            '...',
        'parab_9x41x20':            'Parab_FEA_9by41_r7mm_gmsh.stl',
        'rect_4x41x11':           'Rectangle_FEA_4by41_11wide_r7mm_gmsh.stl',
        'rect_4x41x11_Ch0.1_tall':     '...',
        'rect_4x41x11_Ch0.1_tall_15deg': 'chamfer/new chamfers/15 deg/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.1mm_15deg_gmsh.stl',
        'rect_4x41x11_Ch0.5':     'chamfer/new chamfers/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_gmsh.stl',
        'rect_4x41x11_Ch0.5_thin':'chamfer/new chamfers/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_thin_gmsh.stl',
        'rect_4x41x11_Ch0.5_tall':'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_2mmtop_thinbottom_gmsh.stl',
        'rect_4x41x11_Ch1.0':     'chamfer/new chamfers/Rectangle_FEA_4by41_11wide_with_support_1mmchamfer_gmsh.stl',
        'rect_4x41x20':           '...',
        'rect_9x41x20':           'Rectangle_FEA_9by41_20_r5mm_gmsh.stl',
        'parab':     '...',
        'parab_ang': 'chamfer/new chamfers/4 mains/Parab_FEA_4by41_11wide_with_support_15degAngle_gmsh.stl',
        'parab_ang_comp': 'mapping test meshes/mod test/Parab_FEA_4by41_11wide_with_support_15degAngle_comp_gmsh.stl',
        'parab_ang_SC': 'no chamfer (sanity check)/Parab_FEA_4by41_11wide_with_support_15degAngle_nochamfer_2.5mm_gmsh.stl',
        'parab_ang_SC_crs': 'no chamfer (sanity check)/Parab_FEA_4by41_11wide_with_support_15degAngle_nochamfer_5mm_gmsh.stl',
        'rect':      '...',
        'rect_ang':  'chamfer/new chamfers/4 mains/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.1mm_15deg_coarse_gmsh.stl',
        'rect_ang_comp': 'mapping test meshes/mod test/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.1mm_15deg_coarse_comp_gmsh.stl',
        'parab_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh_gmsh.stl',
        'parab_ang_Ch0.2_crs': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_5mmmesh_gmsh.stl',
        'parab_ang_Ch0.2_fine': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh_gmsh_fine.stl',
        'rect_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_2mmmesh_gmsh.stl',
        'rect_ang_Ch0.2_crs': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_5mmmesh_gmsh.stl',                        
    }
    return variantSTL_names.get(fea_variant, 'FEA STL not found')    # return second arg if fea_variant not found

def fea_variant_VTK (fea_variant):
    variantVTK_names = {
        'parab_4x41x11':            'Parab_FEA_4by41_11wide_r5mm.vtk',
        'parab_4x41x11_Ch0.1_tall': 'chamfer/new chamfers/15 deg/Parab_FEA_4by41_11wide_with_support_0.1mm.vtk',   
        'parab_4x41x11_Ch0.1_tall_15deg': 'chamfer/new chamfers/15 deg/Parab_FEA_4by41_11wide_with_support_15degAngle_0.1mm.vtk',
        'parab_4x41x11_Ch0.5':      'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_0.5mmchamfer.vtk',
        'parab_4x41x11_Ch0.5_thin': 'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN.vtk',
        'parab_4x41x11_Ch0.5_tall': 'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_TALLER.vtk',
        'parab_4x41x11_Ch1.0':      'chamfer/new chamfers/Parab_FEA_4by41_11wide_with_support_1mmchamfer.vtk',
        'parab_4x41x20':            '...',
        'parab_9x41x20':            'Parab_FEA_9by41_r7mm.vtk',
        'rect_4x41x11':             'Rectangle_FEA_4by41_11wide_r7mm.vtk',
        'rect_4x41x11_Ch0.1_tall':     '...',
        'rect_4x41x11_Ch0.1_tall_15deg': 'chamfer/new chamfers/15 deg/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.1mm_15deg.vtk',
        'rect_4x41x11_Ch0.5':       'chamfer/new chamfers/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer.vtk',
        'rect_4x41x11_Ch0.5_thin':  'chamfer/new chamfers/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_thin.vtk',
        'rect_4x41x11_Ch0.5_tall':  'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_2mmtop_thinbottom.vtk',
        'rect_4x41x11_Ch1.0':       'chamfer/new chamfers/Rectangle_FEA_4by41_11wide_with_support_1mmchamfer.vtk',
        'rect_4x41x20':             '...',
        'rect_9x41x20':             'Rectangle_FEA_9by41_20_r5mm.vtk',
        'parab':     '...',
        'parab_ang': 'chamfer/new chamfers/4 mains/Parab_FEA_4by41_11wide_with_support_15degAngle.vtk',
        'parab_ang_comp': 'mapping test meshes/mod test/Parab_FEA_4by41_11wide_with_support_15degAngle_comp.vtk',
        'parab_ang_SC': 'no chamfer (sanity check)/Parab_FEA_4by41_11wide_with_support_15degAngle_nochamfer_2.5mm.vtk',
        'parab_ang_SC_crs': 'no chamfer (sanity check)/Parab_FEA_4by41_11wide_with_support_15degAngle_nochamfer_5mm.vtk',
        'rect':      '...',
        'rect_ang':  'chamfer/new chamfers/4 mains/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.1mm_15deg_coarse.vtk',
        'rect_ang_comp': 'mapping test meshes/mod test/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.1mm_15deg_coarse_comp.vtk',
        'parab_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh.vtk',
        'parab_ang_Ch0.2_crs': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_5mmmesh.vtk',
        'parab_ang_Ch0.2_fine': 'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh_gmsh_fine.vtk',
        'rect_ang_Ch0.2': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_2mmmesh.vtk',
        'rect_ang_Ch0.2_crs': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_5mmmesh.vtk',                        
    }
    return variantVTK_names.get(fea_variant, 'FEA VTK not found')    # return second arg if fea_variant not found

def fea_variant_airSTL (fea_variant):
    variantAirSTL_names = {
        'parab':     'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_ang': 'Parab_FEA_4by41_Air_r10mm_gmsh.stl', # options: r1, r2, r3, r5, r10 (r1 seems best)
        'parab_ang_comp': 'mapping test meshes/mod test/parab_air_comp_gmsh.stl',
        'parab_ang_SC': 'Parab_FEA_4by41_Air_r1mm_gmsh.stl',
        'parab_ang_SC_crs': 'Parab_FEA_4by41_Air_r1mm_gmsh.stl',
        'parab_4x41x11':            'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x11_Ch0.1_tall': 'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x11_Ch0.1_tall_15deg': 'chamfer/new chamfers/0.2 mm chamfer/cavity test/parab_2mm_compliant_Air.stl',
                                          #'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x11_Ch0.5':      'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x11_Ch0.5_thin': 'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x11_Ch0.5_tall': 'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x11_Ch1.0':      'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
        'parab_4x41x20':            '...',
        'parab_9x41x20':            'Parab_FEA_9by41_Air_r7mm_gmsh.stl',
        'rect':     'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_ang': 'new cavities/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_mesh1mm_gmsh.stl', # r1, 2, 3
        'rect_ang_comp': 'mapping test meshes/mod test/rect_air_comp_gmsh.stl',
        #'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl', # 'Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_aug2020_gmsh.stl',
        'rect_4x41x11':             'Rectangle_FEA_4by41_11wide_Air_r5mm_gmsh.stl',
        'rect_4x41x11_Ch0.1_tall':     'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_4x41x11_Ch0.1_tall_15deg': 'new cavities/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_mesh3mm_gmsh.stl',# 'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_4x41x11_Ch0.5':       'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_4x41x11_Ch0.5_thin':  'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_4x41x11_Ch0.5_tall':  'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_4x41x11_Ch1.0':       'chamfer/new chamfers/rectangle test/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_cavityNew_gmsh.stl',
        'rect_4x41x20':             '...',
        'rect_9x41x20':             'Rectangle_FEA_9by41_20_Air_r5mm_gmsh.stl',

        'parab_ang_Ch0.2': 'Parab_FEA_4by41_Air_r1mm_gmsh.stl',
                           #'chamfer/new chamfers/0.2 mm chamfer/cavity test/parab_2mm_compliant_Air.stl',
                           #'Parab_FEA_4by41_Air_r5mm_gmsh.stl',
                           #'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_2mmmesh_Air_gmsh.stl',
        'parab_ang_Ch0.2_crs': 'Parab_FEA_4by41_Air_r1mm_gmsh.stl',
                               #'chamfer/new chamfers/0.2 mm chamfer/Parab_FEA_4by41_11wide_with_support_15degAngle_2mmchamfer_5mmmesh_Air_gmsh.stl',
        'parab_ang_Ch0.2_fine': 'Parab_FEA_4by41_Air_r3mm_gmsh.stl',
                                #'chamfer/new chamfers/0.2 mm chamfer/cavity test/parab_2mm_compliant_Air_crs.stl',
        'rect_ang_Ch0.2': 'new cavities/Rectangle_FEA_4by41_11wide_with_support_0.5mmchamfer_THIN_mesh3mm_gmsh.stl',#'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_2mmmesh_Air_gmsh.stl',
        'rect_ang_Ch0.2_crs': 'chamfer/new chamfers/0.2 mm chamfer/Rectangle_FEA_4by41_11wide_with_support_and_chamfer_0.2mm_15deg_5mmmesh_Air_gmsh.stl',                        
    }
    return variantAirSTL_names.get(fea_variant, 'FEA Air STL not found')    # return second arg if fea_variant not found

def stiffLayerCoords (fea_variant):
    stiffLayerCoords_names = {
        'parab_4x41x11':            '0 -1 0 42 0.75 20',
        'parab_4x41x11_Ch0.1_tall': '-1 -0.5 -1 47 0.2 12',
        'parab_4x41x11_Ch0.1_tall_15deg': '50 -14.2 5 50 -13.2 5 0 0.2 5 15', # box: '-1 -0.5 -1 49 0.2 12', oriented: '50 -13.9 5 50 -12.9 5 0 0.5 5 15'
        'parab_4x41x11_Ch0.5':      '-1 -0.5 -1 47 0.75 12',
        'parab_4x41x11_Ch0.5_thin': '-1 -0.5 -1 47 0.8 12',
        'parab_4x41x11_Ch0.5_tall': '-1 -0.5 -1 47 0.8 12',
        'parab_4x41x11_Ch1.0':      '-1 -0.5 -1 47 1.2 12',
        'parab_4x41x20':            '...',
        'parab_9x41x20':            '...',
        'rect_4x41x11':             '0 -1 0 42 0.75 20',
        'rect_4x41x11_Ch0.1_tall':  '-1 -0.5 -1 47 0.8 12', # check
        'rect_4x41x11_Ch0.1_tall_15deg': '50 -14.2 5 50 -13.2 5 0 0.2 5 15', # box: '-1 -0.5 -1 49 0.2 12'
        'rect_4x41x11_Ch0.5':       '-1 -0.5 -1 47 0.75 12',
        'rect_4x41x11_Ch0.5_thin':  '-1 -0.5 -1 47 0.8 12',
        'rect_4x41x11_Ch0.5_tall':  '-1 -0.5 -1 47 0.8 12',
        'rect_4x41x11_Ch1.0':       '-1 -0.5 -1 47 1.2 12',
        'rect_4x41x20':             '...',
        'rect_9x41x20':             '...',
        'parab':     '...',
        'parab_ang': '50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'parab_ang_comp': '50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'rect':      '...',
        'rect_ang':  '50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'rect_ang_comp':  '50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'parab_ang_Ch0.2':    '50 -14.2 5 50 -13.2 5 0 0.2 5 15', # thick: '50 -13.2 5 50 -12.2 5 0 1.2 5 15'
        'parab_ang_Ch0.2_crs':'50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'parab_ang_Ch0.2_fine':'50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'rect_ang_Ch0.2':     '50 -14.2 5 50 -13.2 5 0 0.2 5 15',
        'rect_ang_Ch0.2_crs': '50 -13.5 5 50 -12.5 5 0 0.9 5 15',
    }
    return stiffLayerCoords_names.get(fea_variant, '0 0 0 0 0 0')


def baseConstraint (fea_variant):
    variantBaseConstraint_names = {
        'parab_4x41x11':            '-5 -5 -5 2 3 25',
        'parab_4x41x11_Ch0.1_tall': '-1 -1 -3 2.5 9 14',
        'parab_4x41x11_Ch0.1_tall_15deg': '3 -5 5 6 9 5 -2 10 5 15', # oriented (rough): '3 -5 5 6 9 5 -2 10 5 15', box: '-1 -3 -3 4 9 14'
        'parab_4x41x11_Ch0.5':      '-1 -1 -3 2.5 9 14',
        'parab_4x41x11_Ch0.5_thin': '-1 -1 -3 2.5 9 14',
        'parab_4x41x11_Ch0.5_tall': '-1 -1 -3 2.5 9 14',
        'parab_4x41x11_Ch1.0':      '-1 -1 -3 2.5 9 14',
        'parab_4x41x20':            '...',
        'parab_9x41x20':            '...',
        'rect_4x41x11':             '-5 -5 -5 2 3 25',
        'rect_4x41x11_Ch0.1_tall':  '-1 -1 -3 2.5 9 14',
        'rect_4x41x11_Ch0.1_tall_15deg':  '3 -5 5 6 9 5 -2 10 5 15', # box: '-1 -1 -3 4 9 14' 
        'rect_4x41x11_Ch0.5':       '-1 -1 -3 2.5 9 14',
        'rect_4x41x11_Ch0.5_thin':  '-1 -1 -3 2.5 9 14',
        'rect_4x41x11_Ch0.5_tall':  '-1 -1 -3 2.5 9 14',
        'rect_4x41x11_Ch1.0':       '-1 -1 -3 2.5 9 14',
        'rect_4x41x20':             '...',
        'rect_9x41x20':             '...',
        'parab':     '...',
        'parab_ang': '3 -5 5 6 9 5 -2 10 5 15',
        'parab_ang_comp': '3 -5 5 6 9 5 -2 10 5 15',
        'parab_ang_SC': '3 -5 5 6 9 5 -2 10 5 15',
        'parab_ang_SC_crs': '3 -5 5 6 9 5 -2 10 5 15',
        'rect':      '...',
        'rect_ang':  '3 -5 5 6 9 5 -2 10 5 15',
        'rect_ang_comp':  '3 -5 5 6 9 5 -2 10 5 15',
        'parab_ang_Ch0.2': '3 -5 5 6 9 5 -2 10 5 15',
        'parab_ang_Ch0.2_crs': '3 -5 5 6 9 5 -2 10 5 15',
        'parab_ang_Ch0.2_fine': '3 -5 5 6 9 5 -2 10 5 15',
        'rect_ang_Ch0.2': '3 -5 5 6 9 5 -2 10 5 15',
        'rect_ang_Ch0.2_crs': '3 -5 5 6 9 5 -2 10 5 15',
    }
    return variantBaseConstraint_names.get(fea_variant, '0 0 0 0 0 0')


def fea_variant_cavity_placement (fea_variant):
    cavity_placements = {
        'parab_4x41x11':            ['40.75 6.5 10', '90 180 0'],          
        'parab_4x41x11_Ch0.1_tall': ['45.55 5.545 9.945', '90 180 0'],                       
        'parab_4x41x11_Ch0.1_tall_15deg':  ['0 0 0', '0 0 -15'], #['47.38 -6.955 9.945', '90 180 -15'],
        'parab_4x41x11_Ch0.5':      ['45.55 6.945 9.945', '90 180 0'],     # could refine
        'parab_4x41x11_Ch0.5_thin': ['45.55 6.445 9.945', '90 180 0'],     # could refine
        'parab_4x41x11_Ch0.5_tall': ['45.55 6.445 9.945', '90 180 0'],     # could refine                        
        'parab_4x41x11_Ch1.0':      ['45.55 6.945 9.945', '90 180 0'],     # could refine
        'parab_4x41x20':            ['0 0 0', '0 0 0'],                    
        'parab_9x41x20':            ['40.75 10.89 19', '90 180 0'],        
        'rect_4x41x11':             ['0.75 7 1', '90 0 0'],                
        'rect_4x41x11_Ch0.1_tall':  ['4.7 1 1', '0 0 0'],
        'rect_4x41x11_Ch0.1_tall_15deg':  ['6.51 -1.64 1', '0 0 -15'], # if not angled: '6.71 0.10 1', '0 0 0'
        'rect_4x41x11_Ch0.5':       ['4.7 1.5 1', '0 0 0'],
        'rect_4x41x11_Ch0.5_thin':  ['4.7 1 1', '0 0 0'],
        'rect_4x41x11_Ch0.5_tall':  ['4.7 1 1', '0 0 0'],
        'rect_4x41x11_Ch1.0':       ['4.7 1.5 1', '0 0 0'],
        'rect_4x41x20':             ['0 0 0', '0 0 0'],
        'rect_9x41x20':             ['0.75 10.89 1', '90 0 0'],
        'parab':     '...',
        'parab_ang':  ['47.38 -6.955 9.945', '90 180 -15'],
        'parab_ang_comp':  ['0.0 0.0 0.0', '0 0 -15'],
        'parab_ang_SC':  ['47.38 -6.955 9.945', '90 180 -15'],
        'parab_ang_SC_crs':  ['47.38 -6.955 9.945', '90 180 -15'],
        'rect':      '...',
        'rect_ang':  ['7.107 -1.709 1', '0 0 -15'], # original: '6.507 -1.639 1'; twist-comp: '7.107 -1.709 1'
        'rect_ang_comp':  ['0 0 0', '0 0 -15'],
        'parab_ang_Ch0.2':      ['47.38 -6.955 9.945', '90 180 -15'],
        'parab_ang_Ch0.2_crs':  ['47.38 -6.955 9.945', '90 180 -15'], #['0 0 0', '0 0 -15'],
        'parab_ang_Ch0.2_fine': ['47.38 -6.955 9.945', '90 180 -15'],
        'rect_ang_Ch0.2':      ['6.51 -1.64 0.65', '0 0 -15'], #['6.51 -1.64 1', '0 0 -15'],
        'rect_ang_Ch0.2_crs': ['0 0 0', '0 0 -15'],
    } # translations in mm, rotations in deg
    return cavity_placements.get(fea_variant, ['0 0 0', '0 0 0'])    # return second arg if fea_variant not found


def fea_variant_probe_indices (fea_variant):
    probeIndices_names = {
        'parab_4x41x11':            '151 156 161 166 175',
        'parab_4x41x11_Ch0.1_tall': '984 1174 1168 1162 1064',
        'parab_4x41x11_Ch0.1_tall_15deg': '998 1188 1182 1176 1078',
        'parab_4x41x11_Ch0.5':      '169 174 180 186 192',
        'parab_4x41x11_Ch0.5_thin': '169 174 180 186 192',
        'parab_4x41x11_Ch0.5_tall': '169 174 180 186 192',
        'parab_4x41x11_Ch1.0':      '165 170 176 182 190',
        'parab_4x41x20':            '...',
        'parab_9x41x20':            '...',
        'rect_4x41x11':             '...',
        'rect_4x41x11_Ch0.1_tall':  '155 160 166 171 179',
        'rect_4x41x11_Ch0.1_tall_15deg':  '1078 1088 1100 1110 988', # note: slightly diff. node spacing bc mesh
        'rect_4x41x11_Ch0.5':       '155 160 166 171 179',
        'rect_4x41x11_Ch0.5_thin':  '155 160 166 171 179',
        'rect_4x41x11_Ch0.5_tall':  '155 160 166 171 179',
        'rect_4x41x11_Ch1.0':       '152 157 162 167 175',
        'rect_4x41x20':             '...',
        'rect_9x41x20':             '...',
        'parab':     '...',
        'parab_ang':  '347 352 363 557 1', # was: 485 503 578 556 544
        'parab_ang_comp': '485 503 578 556 544',
        'parab_ang_SC':  '1265 1323 1317 1222 6',
        'parab_ang_SC_crs':  '503 516 513 483 4',
        'rect':      '...',
        'rect_ang':  '613 616 540 587 575',
        'rect_ang_comp':  '613 616 540 587 575', # left, right, center (r1mm cavity)
        'parab_ang_Ch0.2': '1537 1272 1576 1596 1618   1536 1008 1027 1049 1651  1527 1802 1795',# 1805 1799 1792 1855', #with r5mm cavity: '3099 2783',#'485 503 578 556 544',
        'parab_ang_Ch0.2_crs': '485 503 578 556 544',
        'parab_ang_Ch0.2_fine': '0',
        'rect_ang_Ch0.2': '613 616 540 587 575',
        'rect_ang_Ch0.2_crs': '613 616 540 587 575',
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
        'cyl_d100_cut': 'cyl_d100_cut_r30mm_gmsh.stl',
        'hemi_d50':  '...',
        'hemi_d100': '...',
        'hemi_d200': '...',
    }
    return objSTLs.get(obj_variant, '(Object STL not found)')

def obj_variant_VTK (obj_variant):
    objVTKs = {
        'cyl_d50':   '...',
        'cyl_d100':  'cyl_d100_r10mm.vtk', # r3, r10
        'cyl_d200':  'cyl_d200_r15mm.vtk',
        'cyl_d100_cut': 'cyl_d100_cut_r30mm.vtk',
        'hemi_d50':  '...',
        'hemi_d100': '...',
        'hemi_d200': '...',
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
        'cyl_d100_cut': ['-63 -49 17.5', '-90 0 0'],  # normal: -50 -52.5 17.5, offset: '-63 -49 17.5'
        'hemi_d50':  ['0 0 0', '0 0 0'],
        'hemi_d100': ['0 0 0', '0 0 0'],
        'hemi_d200': ['0 0 0', '0 0 0'],
    } # first element: translation (x y z, mm), second element: rotation (x y z, deg)
    return obj_positions.get(obj_variant, ['0 0 0', '0 0 0'])

def obj_constraint (obj_variant):
    obj_boxROI = {
        'cyl_d50':  '...',
        'cyl_d100': '-70 -100 -15 40 -80 25', # ymax: -60 for higher, -80 for lower
        'cyl_d200': '-120 -210 -15 105 -160 25',
        'cyl_d100_cut': '-60 -55 -35 60 -30 30',
        'hemi_d50': '...',
        'hemi_d100': '...',
        'hemi_d200': '...',
    } # boxROI coords: 'xmin ymin zmin xmax ymax zmax'
    return obj_boxROI.get(obj_variant, '0 0 0 0 0 0')

def obj_addConstraint (obj_variant):
    obj_boxROI = {
        'cyl_d50':  '...',
        'cyl_d100': '-70 -80 -15 -25 0 25',
        'cyl_d200': '-70 -100 -15 -25 0 25',
        'cyl_d100_cut': '...',
        'hemi_d50': '...',
        'hemi_d100': '...',
        'hemi_d200': '...',
    } # boxROI coords: 'xmin ymin zmin xmax ymax zmax'
    return obj_boxROI.get(obj_variant, '0 0 0 0 0 0')

def obj_probeIndices (obj_variant):
    obj_indices = {
        'cyl_d50':  '0',
        'cyl_d100': '137 130 122 115 107', # r10mm
        'cyl_d200': '198 192 186 179 173 167', # r15mm, base: 204
    }
    return obj_indices.get(obj_variant, '0 0 0 0 0')

