------------------------------------------------------------------
# E-Test

'testdata': 'Current'

------------------------------------------------------------------
# Focus Test/ Focus Check

'testdata': 'PTC Value'

------------------------------------------------------------------
# Calibration ( 3030 / 6060 )

'testdata': [
                'PIXEL(40,30)', 
                'Summary'
            ]

------------------------------------------------------------------
# Calibration (3060)
'testdata': [
                'VDD', 
                'AMBIENT_hi', 
                'AMBIENT_lo', 
                'SCENE_hi', 
                'SCENE_Avg', 
                'SCENE_lo', 
                'RESULT_SUMMARY',                       ## this includes sensitivity
                'AMBIENT_median'
            ]
------------------------------------------------------------------
# Calibration (2237)

'testdata': [
                'VDD', 
                'AMBIENT_hi', 
                'AMBIENT_lo', 
                'SCENE_hi', 
                'SCENE_Avg', 
                'SCENE_lo', 
                'RESULT_SUMMARY',                       ## this includes sensitivity
                'AMBIENT_median'
            ]

------------------------------------------------------------------
# other parameters available on the Calibration 3030/6060/3060/2237 station
# currently the following data are not added to test data
# they can be added if there is in needed

optional_data = 
{
    'gui_version': 'GUI Version',                       # PRoduction GUI verison
    'fw_version': 'Firmware Version',                   # Jig MCU boards FW
    #'module_type': 'Module Type',                      # Meridian Product code in the future; not output by jig yet
    'socket_position': 'Position',                      # Socket position in the jig
    'wafer_number': 'Wafer Number',
    'wafer_coord_x': 'WaferCoord X',
    'wafer_coord_y': 'WaferCoord Y',
    'wafer_error_code': 'WaferErrorCode',               # Error code from CP3 wafer-level testing
}
