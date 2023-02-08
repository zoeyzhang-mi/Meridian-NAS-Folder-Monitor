# Monitor Path
#path = r"C:/Users/meridian/Desktop/Test Folder"
path_to_track = r"/home/zoey/production_data/test_data"

#script path (saving Pointers.json)
script_path = r"/home/zoey/production_data/Meridian_Folder_Monitor"

# Post URL
# url = r'http://10.143.4.218/B3J001/M3J001Uplod1/Uploaddata'
# url = r'https://httpbin.org/get'
#url = r'http://localhost:8000/test'
url = r'http://192.168.50.131:5000'

# Start parsing the data if there are no more modifications within X sec
countdown_time_set = 4 # in sec

# Waiting time for each server respond
time_out = 10 # in sec

# Print out the server response
bool_print_response = True

# Print out the posted data to the server
bool_print_response_content = True

# Slash r'/' or Backslash '\\'
slash = r'/'
