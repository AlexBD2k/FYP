#@authors: Michelle Collins
from event_data_processing import event_data_processing
from pipeline_globals import *
import mne
import os
from pipeline_preprocessing import *
from rename_raw_data import rename_raw_data
from repair_event_data import *

rename_raw_data()

for subject in subjects:
    for trial in trials:
        for task in tasks:
            print("Now pipelining subject: " + subject + ", trial: " + trial + ", task: " + task)
            file_name = "{}_{}_{}.bdf".format(subject, trial, task)
            file_loc = os.path.join(folder_loc, subject, file_name)
            
            raw = mne.io.read_raw_bdf(file_loc, preload=True)
            raw = preprocessing(raw)
            
            if subject in to_be_repaired:
                try:
                    raw = repair_event_data(subject, trial, task, raw)
                except FileNotFoundError as e:
                    print(e)
                    
            raw = event_data_processing(raw, task)
            file_name_cleaned = "{}_{}_{}_(Cleaned).fif".format(subject, trial, task)
            file_loc = os.path.join(folder_loc, subject, file_name_cleaned)
            raw.save(file_loc, overwrite=True)
            print("Cleaned file " + file_name_cleaned + " saved")