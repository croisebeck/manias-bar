import csv
import os
import numpy as np

# Gets all days between December 2017 to December 2019
days_range = np.arange('2018-11', '2019-12', dtype='datetime64[D]')

# print(days_range);

manias_times = []
stannis_times = []
bk_times = []

# Open .csv files and get all Manias and Stannis entries
for file in os.listdir("./files/"):
    with open("./files/" + file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[2] == "Restaurante Manias":
                manias_times.append([row[0], float(row[3])])  # Save date and expense
            elif row[2] == "Stannis Pub":
                stannis_times.append([row[0], float(row[3])])  # Save date and expense
            elif row[2] == "Burger King":
                bk_times.append([row[0], float(row[3])])  # Save date and expense
print("✔ Nubank data")
manias_times.sort(key=lambda tup: tup[0])
stannis_times.sort(key=lambda tup: tup[0])
bk_times.sort(key=lambda tup: tup[0])
print("✔ Data sorted")

manias_data = []
stannis_data = []
bk_data = []
day_amount = 0

# Check multiple entries for the same day (Manias)
for i in range(len(manias_times)):
    if i < len(manias_times) - 1:
        if manias_times[i][0] == manias_times[i + 1][0]:
            day_amount = day_amount + manias_times[i][1]
        else:
            day_amount = day_amount + manias_times[i][1]
            manias_data.append([manias_times[i][0], day_amount])
            day_amount = 0
    else:
        day_amount = day_amount + manias_times[i][1]
        manias_data.append([manias_times[i][0], day_amount])
        day_amount = 0

day_amount = 0
# Check multiple entries for the same day (Stannis)
for i in range(len(stannis_times)):
    if i < len(stannis_times) - 1:
        if stannis_times[i][0] == stannis_times[i + 1][0]:
            day_amount = day_amount + stannis_times[i][1]
        else:
            day_amount = day_amount + stannis_times[i][1]
            stannis_data.append([stannis_times[i][0], day_amount])
            day_amount = 0
    else:
        day_amount = day_amount + stannis_times[i][1]
        stannis_data.append([stannis_times[i][0], day_amount])
        day_amount = 0

# Check multiple entries for the same day (bk)
for i in range(len(bk_times)):
    if i < len(bk_times) - 1:
        if bk_times[i][0] == bk_times[i + 1][0]:
            day_amount = day_amount + bk_times[i][1]
        else:
            day_amount = day_amount + bk_times[i][1]
            bk_data.append([bk_times[i][0], day_amount])
            day_amount = 0
    else:
        day_amount = day_amount + bk_times[i][1]
        bk_data.append([bk_times[i][0], day_amount])
        day_amount = 0

m = 0  # Index to manias
s = 0  # Index to Stannis
b = 0  # Index to bk

# manias_hist = []
# stannis_hist = []

series = [["Date", "Manias", "Stannis", "bk"]]

# For each day in the range get from file
for date in days_range:
    manias_value = 0
    stannis_value = 0
    bk_value = 0
    # Manias data
    if m < len(manias_data):
        if str(date) == manias_data[m][0]:
            manias_value = manias_data[m][1]
            # manias_hist.append(manias_data[m])
            m = m + 1
        else:
            manias_value = 0.0
            # manias_hist.append([str(date), 0.0])

    # Stannis data
    if s < len(stannis_data):
        if str(date) == stannis_times[s][0]:
            stannis_value = stannis_times[s][1]
            # stannis_hist.append(stannis_times[s])
            s = s + 1
        else:
            stannis_value = 0.0
            # stannis_hist.append([str(date), 0.0])

    # bk data
    if m < len(bk_data):
        if str(date) == bk_data[m][0]:
            bk_value = bk_data[m][1]
            # bk_hist.append(bk_data[b])
            b = b + 1
        else:
            bk_value = 0.0
            # bk_hist.append([str(date), 0.0])

    series.append([date, manias_value, stannis_value, bk_value])

manias_amount = 0
stannis_amount = 0
bk_amount = 0

for prices in series:
    if prices[0] != "Date":
        manias_amount = manias_amount + prices[1]
        stannis_amount = stannis_amount + prices[2]
        bk_amount = bk_amount + prices[3]

with open('./data/manias_stannis_series.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(series)
csvFile.close()
print("✔ Data file saved")
print("Number of days analysed: " + str(len(days_range)))
print("Amount spend at Manias: R$ %.2f" % manias_amount)
print("Amount spend at Stannis: R$ %.2f" % stannis_amount)
print("Amount spend at bk: R$ %.2f" % bk_amount)
print("Number of days Manias : " + str(len(manias_data)))
print("Number of days Stannis : " + str(len(stannis_times)))
print("Number of days bk : " + str(len(bk_data)))
print("*** DONE ***")