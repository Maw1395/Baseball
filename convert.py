import csv
import sqlite3

from glob import glob; from os.path import expanduser
conn = sqlite3.connect( # open "places.sqlite" from one of the Firefox profiles
	glob(expanduser('../project.db'))[0]
)
cursor = conn.cursor()
for year in range(2007,2018):
	cursor.execute("select * from PlateAppearance where year="+str(year))
	#with open("out.csv", "w", newline='') as csv_file:  # Python 3 version
	with open(str(year)+".csv", "wb") as csv_file:              # Python 2 version
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor.description]) # write headers
		csv_writer.writerows(cursor)
