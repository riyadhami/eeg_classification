**Import the require library**
pip install os<br/>
pip install mne<br/>
pip install numpy<br/>
pip install scipy<br/>
pip install matplotlib<br/>
pip install skfeature-chappers<br/>

<br/>
# Define the base folder path where the data is located
folder_path = "D:\SSVEP-based-EEG-signal-processing\Data" 
path_files, files, folders = Data_path.data_path(folder_path, data_format="gdf") 
path_files
