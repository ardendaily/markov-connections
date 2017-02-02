nodupes = []

with open("./craigslinks.txt", "r") as file:
	urls = file.read().split("\n")
	for url in urls:
		if url not in nodupes:
			nodupes.append(url)

with open("./craigslinks_nodupes.txt", "w+") as writer:
	for url in nodupes:
		writer.write(url+"\n")
