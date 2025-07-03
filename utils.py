"""
Written by Arindam Saha, ANU, 2025
github: arindam5aha, arindam96@outlook.com
"""

import bz2, pickle
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc
import random
import glob
from scipy.signal import find_peaks

def save_bz2(data, filename='./data/run_data.bz2'):
    file = bz2.BZ2File(filename, 'wb')
    file.write(pickle.dumps(data, protocol=4))
    file.close()

def load_bz2(filename='./data/run_data.bz2'):
    file = bz2.BZ2File(filename, 'rb')
    dd = pickle.loads(file.read())
    file.close()
    return dd

def get_datetime():
    return str(datetime.now().strftime("%b%d_%H-%M"))

def topk(values, k):
    idxs = np.argpartition(np.array(values), -k)[-k:]
    topk_vals = values[idxs]
    return topk_vals, idxs

def plot_in_dark_mode():
    plt.style.use(['dark_background', 'bmh'])
    plt.rc('axes', facecolor='k')
    plt.rc('figure', facecolor='k')
    
def argmax_height(data):
    max_height = 0.0
    max_height_idx = 0    
    for i, o in enumerate(data):
        if np.max(o) > max_height:
            max_height = np.max(o)
            max_height_idx = i
    return max_height_idx, max_height
    
def allign_traces(data, ref_trace=None, height=0.5, width=2):
    # alligns temp drifted traces to the trace with max height    
    peaks = []
    if ref_trace is None:
        idx, _ = argmax_height(data)
        ref_trace = data[idx]
    align_to_idx = np.argmax(ref_trace)
    for i, o in enumerate(data):
        peak, _  = find_peaks(o, height=height)
        if len(peak) > 0:
            peaks.append(peak[0])
        else:
            peaks.append(0)
    corrected_traces = []
    last_idx = peaks[0]
    for idx, obs in zip(peaks, data):
        if idx != 0:
            last_idx = idx
        corrected_traces.append(np.roll(obs, align_to_idx - last_idx))
    corrected_traces = np.array(corrected_traces)
    
    corrs = []
    for o in corrected_traces:
        corrs.append(np.correlate(o, ref_trace))         # Integral of the in-place multiplication of the two traces
    corrs = np.array(corrs)
    
    return corrected_traces

def max_till(data, length=None):
    if length is None:
        length = len(data)
    max_ = data[0]
    max_till = []
    for r in data:
        if r > max_:
            max_ = r
        max_till.append(max_)
    if len(max_till) < length:
        max_till = max_till + [max_]*(length - len(max_till))
    max_till = np.array(max_till)
    return max_till