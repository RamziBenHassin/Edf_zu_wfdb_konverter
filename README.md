# Edf_zu_wfdb_konverter

This program has a main goal to convert edf file to wfdb (mit), based a command line Terminal 

## Setup 
Some required libraries should be installed previously 
- WFDB: https://github.com/MIT-LCP/wfdb-python 
- MNE: https://mne.tools
- pyEDFlib: https://pypi.org/project/pyEDFlib

these libraries could be installed by executing this following command 

### `pip install -r requirements.txt`

## Running the files 
Through a simple command line the conversion will take place and generate two files .data and .hea 
### `python edf2wfdb.py -i <path> -o file_name` 

Or by executing this following command 
### `edf2wfdb.exe -i <path> -o file_name` 

<br> With `<path>` referencing the path of the edf file that we want to convert <br> and `file_name` the wfdb file name



