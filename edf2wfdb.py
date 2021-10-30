import mne
import pandas as pd
import wfdb
import pyedflib

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)
p = parser.parse_args()
file = str(p.file_path)

print("Enter the Wfdb_file name")
s = input()
file = str(p.file_path)

file_name = str(s)

data = mne.io.read_raw_edf(file)
raw_data = data.get_data()

info = data.info

channels = data.ch_names

f = pyedflib.EdfReader(file)

fsx = f.getSampleFrequency(1)
print(fsx)

edf_dataframe = pd.DataFrame(raw_data)

edf_data = edf_dataframe.T

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

