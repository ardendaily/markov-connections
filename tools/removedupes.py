from sys import argv

nodupes = []

with open(argv[1], "r") as file:
	urls = file.read().split("\n")
	for url in urls:
		if url not in nodupes:
			nodupes.append(url)

for url in nodupes:
	print url
