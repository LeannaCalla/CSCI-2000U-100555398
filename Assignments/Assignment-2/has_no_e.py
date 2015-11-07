def has_no_e(line):
	for i in line:
		if i == 'e':
			return (False)
	return (True)

reader = open ('gadsby_stripped.txt','r')
for line in reader:
	has_no_e(line)
reader.close()
