import csv
file = open("ThreatTemplate.csv","a",newline='')
writer = csv.writer(file)
title = ["Persistence","additional malwares", "CVE"]
writer.writerow(title)

List = []
List.append(("T1055" + "-" + "Remote access trojan" + "\nhello","RAT","CVE-2022"))
writer.writerows(List)
file.close