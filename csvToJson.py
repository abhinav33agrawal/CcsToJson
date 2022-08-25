import csv
def convertCSVtoJSON(datas):

    # function to read csv file and return a dict so that we can further work on the data
    decoded_file = datas.read().splitlines()
    reader = csv.DictReader(decoded_file)
    output = []
    for each in reader:
        output.append(each)
    return output

f = open("test.csv")

data = convertCSVtoJSON(f)
print(data)
