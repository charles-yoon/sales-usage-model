import pandas as pd
import os

# remove identifying features such as "ctas_official_version"
folders = ["./data/sessions-active_30-by_device/",
           "./data/sessions-active_30-canada/",
           "./data/units-active_devices-by_device/",
           "./data/units-active_devices-canada/"]

os.getcwd()
# os.listdir("../data/sessions-active_30-by_device/")[0:5]
# for folder in folders:
#     for file in os.listdir(folder):
#         new_name = file.replace("ctas_official_version-", "")
#         os.rename(folder + file, folder + new_name)

# navigate to directory and combine all csv files
data = []
for folder in folders:
    info = pd.DataFrame()
    for file in os.listdir(folder):
        input_data = pd.read_csv(folder + file, skiprows=4)
        info = pd.concat([info, input_data], ignore_index=True)

    data.append(info)

# write combined tables to file
# data[0].to_csv("sessions-active_30-by_device.csv", index=False)
# data[1].to_csv("sessions-active_30-canada.csv", index=False)
# data[2].to_csv("units-active_devices-by_device.csv", index=False)
# data[3].to_csv("units-active_devices-canada.csv", index=False)

# combine datasets
active_sessions = pd.merge(data[0], data[1], on="Date")
units = pd.merge(data[2], data[3], on="Date")

# active_sessions.to_csv("active_sessions.csv", index=False)
# units.to_csv("units.csv", index=False)

# reform table to have
# 1. usage by device
# 2. usage by canada vs. rest of world
# 3. combine 1 and 2?
# 4. repeat using active devices
