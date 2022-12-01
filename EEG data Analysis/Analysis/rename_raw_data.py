import os
from pipeline_globals import *

def rename_raw_data():

    for folder in os.listdir(folder_loc):
        if folder in blacklist_folders:
            continue
    
    if folder in subjects:
        for file in os.listdir(folder_loc + folder):
            
            subject = folder
                
            if "_1_SG".lower() in file.lower() or \
            "_1_VS".lower() in file.lower() or \
            "_1_VPA".lower() in file.lower() or \
            "_2_SG".lower() in file.lower() or \
            "_2_VS".lower() in file.lower() or \
            "_2_VPA".lower() in file.lower():
                print("File " + file + " already exists")
                continue

            if ".bdf".lower() not in file.lower():
                continue
                
            #This takes each file and assigns its trial as 1 or 2,
            # depending on whether or not the string "Exp2b" is in the original name
            if "Exp2b".lower() in file.lower():
                trial = "2"
            else:
                trial = "1"
                
            #identifies which task it is
            if " VPA".lower() in file.lower():
                task = "VPA"
            elif "Spatial".lower() in file.lower():
                task = "SG"
            elif "Visual Search".lower() in file.lower():
                task = "VS"
            elif "finger".lower() in file.lower():
                continue
            elif "eyes".lower() in file.lower():
                continue
            
            #flags files which may not fall into original naming convention
            else:
                print("Did not find task for " + file)
                continue
        
            old_filename = os.path.join(folder_loc, folder, file)
            new_filename = f"D:\\{subject}\\{subject}_{trial}_{task}.bdf"
            print("Renaming " + old_filename + " to: " + new_filename )
            os.rename(old_filename, new_filename)
            print("finished renaming")