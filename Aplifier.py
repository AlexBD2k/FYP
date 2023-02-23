# Variables should contain the location of the EEG files,
# as well as the subjects, and trials that you wish to get amplitude data
subjects = ["20", "52", "55", "56", "58", "59", "60", "61"]
trials = ["2"]
tasks = ["VPA"]
folder_loc = f"C:\\"
VPA_picks = ["PO3", "PO4", "Pz"]
task = "VPA"
window = [0.2,0.4]

for subject in subjects:
    print(subject)
    for trial in trials:
        file_name = "{}_{}_{}_(Cleaned).fif".format(subject, trial, task)
        file_loc = os.path.join(folder_loc, subject, file_name)
        raw = mne.io.read_raw_fif(file_loc, preload=True)
        events = mne.find_events(raw, stim_channel='Status')
        
        event_dict = {
        'false/congruent/correct': 12, 'false/congruent/incorrect': 13,
        'false/incongruent/correct': 14, 'false/incongruent/incorrect': 15,
        'true/congruent/correct': 16, 'true/congruent/incorrect': 17,
        'true/incongruent/correct': 18, 'true/incongruent/incorrect': 19}
        
        epochs = mne.Epochs(raw, events, event_id=event_dict, tmin=window[0], tmax=window[1], \
            baseline = None, preload=True, on_missing='ignore', decim=4)
        
    for item in event_dict:
        item_epochs = epochs[item]
        evoked_response = item_epochs.average()
        evoked_response.plot(picks = VPA_picks)
        
        #Printing PO3
        evoked_response.set_channel_types({'Fp1': "misc", 'AF3': "misc", 'F7': "misc", 'F3': "misc",
        'FC1': "misc",\
        'FC5': "misc", 'T7': "misc", 'C3': "misc", 'CP1': "misc", 'CP5': "misc",\
        'P7': "misc", 'P3': "misc", 'O1': "misc", 'Oz': "misc", 'O2': "misc", 'P4': "misc",\
        'P8': "misc", 'CP6': "misc", 'CP2': "misc", 'C4': "misc", 'T8': "misc", 'FC6': "misc", \
        'FC2': "misc", 'F4': "misc", 'F8': "misc", "PO4" : "misc", "Pz" : "misc", 'AF4': "misc", \
        'Fp2': "misc", 'Fz': "misc", 'Cz': "misc", "PO3" : "eeg"})
        
        #print(item)
        try:
            print(evoked_response.get_peak(ch_type = "eeg" , mode = "pos"))
        except ValueError:
            print("Didnt find epochs of " + item)
            
        #Printing PO4
        evoked_response.set_channel_types({'Fp1': "misc", 'AF3': "misc", 'F7': "misc", 'F3': "misc",
        'FC1': "misc",\
        'FC5': "misc", 'T7': "misc", 'C3': "misc", 'CP1': "misc", 'CP5': "misc",\
        'P7': "misc", 'P3': "misc", 'O1': "misc", 'Oz': "misc", 'O2': "misc", 'P4': "misc",\
        'P8': "misc", 'CP6': "misc", 'CP2': "misc", 'C4': "misc", 'T8': "misc", 'FC6': "misc", \
        'FC2': "misc", 'F4': "misc", 'F8': "misc", "PO3" : "misc", "Pz" : "misc", 'AF4': "misc", \
        'Fp2': "misc", 'Fz': "misc", 'Cz': "misc", "PO4" : "eeg"})
        
        try:
            print(evoked_response.get_peak(ch_type = "eeg" , mode = "pos"))
        except ValueError:
            print("Didnt find epochs of " + item)
            
        #Printing Pz
        evoked_response.set_channel_types({'Fp1': "misc", 'AF3': "misc", 'F7': "misc", 'F3': "misc",
        'FC1': "misc",\
        'FC5': "misc", 'T7': "misc", 'C3': "misc", 'CP1': "misc", 'CP5': "misc",\
        'P7': "misc", 'P3': "misc", 'O1': "misc", 'Oz': "misc", 'O2': "misc", 'P4': "misc",\
        'P8': "misc", 'CP6': "misc", 'CP2': "misc", 'C4': "misc", 'T8': "misc", 'FC6': "misc", \
        'FC2': "misc", 'F4': "misc", 'F8': "misc", "PO4" : "misc", "PO3" : "misc", 'AF4': "misc", \
        'Fp2': "misc", 'Fz': "misc", 'Cz': "misc", "Pz" : "eeg"})
        
        try:
            print(evoked_response.get_peak(ch_type = "eeg" , mode = "pos" ))
        except ValueError:
            print("Didnt find epochs of " + item)