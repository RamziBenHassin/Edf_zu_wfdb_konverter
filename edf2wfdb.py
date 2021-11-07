from pathlib import Path
import mne
import pandas as pd
import wfdb
import pyedflib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--file_path", type=Path, help="enter the edf_file path")
parser.add_argument('-o', "--file_name", help="enter the wfdb_file name")

p = parser.parse_args()
file = str(p.file_path)
file_name = str(p.file_name)

data = mne.io.read_raw_edf(file)
raw_data = data.get_data()
print(raw_data)

info = data.info
print(info)

channels = data.ch_names

f = pyedflib.EdfReader(file)
fsx = f.getSampleFrequency(1)

edf_dataframe = pd.DataFrame(raw_data)
edf_data = edf_dataframe.T
print(edf_data)

fmtx = []
adc_gainx = []
baselinex = []
unitsx = []

for i in range(len(channels)):
    fmtx.append('16')
    adc_gainx.append(0)
    baselinex.append(0)
    unitsx.append('mV')

numArr = edf_data.to_numpy()

wfdb.wrsamp(file_name, fs=fsx, units=unitsx, sig_name=channels, p_signal=numArr, fmt=fmtx)


