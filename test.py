import pandas as pd
import csv

csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Age','Height','Weight'])


name = ["hello", "bye", "die"]
age = [ 0, 4, 6]
height = [500, 60, 20329]
weight = [232, 345, 232352]

for i in range (0, 3):
    csv_writer.writerow([name[i], age[i], height[i], weight[i]])

csv_file.close()

result = pd.read_csv('test.csv')

print(result)


stringA = 'àa string withé fuünny charactersß.'

encodestring = stringA.encode('ascii', 'ignore')
decodedstring = encodestring.decode()
print(encodestring)
print(decodedstring)