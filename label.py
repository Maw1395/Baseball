import csv
def main(year):
	label = ['Labels']
	inning = 1
	cpitch = ''
	num = 0
	game = 1000
	ls1 = 0
	ls2 = 0

	with open(str(year)+'-outappend.csv', 'rb') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			
			if num == 0:
				num = num + 1
				label.append('0')
				continue
			if float(row[11])==999:
				continue
			label.append('0')

			if game != int(row[2]):
				game = int(row[2])
				pitcher1 = row[4]
				pitcher2 = ''
				inning = 1
				label[ls1] = '1'
				label[ls2] = '1'

			if pitcher1 != row[4] and game == int(row[2]) and pitcher2 == '':
				pitcher2 = row[4]

			if row[4] == pitcher1:
				cpitch = row[4]
				ls1 = num

			if row[4] == pitcher2:
				cpitch = row[4]
				ls2 = num

			num = num + 1
		label[ls1] = '1'
		label[ls2] = '1'
	label[0] = "L"
	label[1] = '0'
	del label[-1]
	with open(str(year)+"-Labels1.csv", "wb") as csv_file:
		writer = csv.writer(csv_file)
		for line in label:
			writer.writerow(line)

if __name__=="__main__":
	for year in range(2007,2018):
		main(year)