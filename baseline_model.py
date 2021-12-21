import csv
import preprocessing
from sklearn.metrics import*


def main():
    rvws = []
    labels = []

    #Load in reviews and labels
    with open("review.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        line = 0

        for row in csv_reader:
            if(line == 0):
                line += 1
            else:
                rvws.append(row[0])
                labels.append(row[1])
                line += 1

        print(line - 1, " reviews loaded")


    data = preprocessing.ProcessedData()
    mostFreqRating = getMostRating(data.y_train)
    predictions = []
    for i in data.y_dev:
        predictions.append(mostFreqRating)

    P = precision_score(y_true=data.y_dev, y_pred=predictions, average="micro")
    fp = '{0:.4g}'.format(P)
    R = recall_score(y_true=data.y_dev, y_pred=predictions, average="micro")
    fr = '{0:.4g}'.format(R)
    F1 = f1_score(y_true=data.y_dev, y_pred=predictions, average="micro")
    ff1 = '{0:.4g}'.format(F1)
    print("Dev set evaluation:")
    print("Micro Scale: \nPrecision = ", fp, " | Recall = ", fr, " | F1-Score = ", ff1)



#Returns the rating with the highest number of appearances in the dataset
def getMostRating(dataset):
    ratings = [0, 0, 0, 0, 0]
    for i in dataset.iteritems():
        value = i[1]
        if(value == 1):
            ratings[0] += 1
        elif(value == 2):
            ratings[1] += 1
        elif(value == 3):
            ratings[2] += 1
        elif(value == 4):
            ratings[3] += 1
        elif(value == 5):
            ratings[4] += 1
    highest = 0
    index = 0
    print(ratings)
    for i in range(len(ratings)):
        if(ratings[i] > highest):
            highest = ratings[i]
            index = i + 1
    print(str(index) + "-Star appears the most with " + str(highest) + " appearances.")
    return index


main()