import csv
import preprocessing
from sklearn.metrics import*
import pandas as pd

#Set to slightly above actual values, shortent these if we want to 
#eval and train on subsections.
NUM_TRAIN = 210000
NUM_EVAULUATE = 46000


def main():
    #Load the data
    data = preprocessing.ProcessedData()
    CalcMaxEntBaseline()
    CalcNaiveBayesBaseline(data)


#Generates the MaxEnt Baseline model and evauluates it. 
def CalcMaxEntBaseline():
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
                labels.append(int(row[1]))
                line += 1

        print(line - 1, " reviews loaded")

    train_labels = pd.Series(labels[:35000])
    dev_eval_labels = pd.Series(labels[35000:50000])

    rating = getMostRating(train_labels)
    predictions = GeneratePredictionns(dev_eval_labels, rating)
    Evauluate(predictions, dev_eval_labels, model="MaxEnt Baseline Model")


#Takes in the preprocessed data used by the Naive Bayes model and makes a baseline model
#as well as evaulautes it.
def CalcNaiveBayesBaseline(data):
    trainingData = data.y_train[:NUM_TRAIN]
    mostFreqRating = getMostRating(trainingData)

    #Get the dev data we want to use and guess the most frequent label on it
    devData = data.y_dev[:NUM_EVAULUATE]
    predictions = GeneratePredictionns(devData, mostFreqRating)
    Evauluate(devData, predictions, model="Naive Bayes Baseline Model")

   
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
    for i in range(len(ratings)):
        if(ratings[i] > highest):
            highest = ratings[i]
            index = i + 1
    print(str(index) + "-Star appears the most with " + str(highest) + " appearances.")
    return index

#Generates predictions for the baseline model by guessing the most common rating for
#each entry in the dev data
def GeneratePredictionns(data, rating):
    predictions = []
    for i in data:
        predictions.append(rating)

    return predictions

#Evaluates the model given its predictions and dev data.
def Evauluate(predictions, data, model=None):
    P = precision_score(y_true=data, y_pred=predictions, average="micro")
    fp = '{0:.4g}'.format(P)
    R = recall_score(y_true=data, y_pred=predictions, average="micro")
    fr = '{0:.4g}'.format(R)
    F1 = f1_score(y_true=data, y_pred=predictions, average="micro")
    ff1 = '{0:.4g}'.format(F1)
    print("Dev set evaluation for " + model + ":")
    print("Micro Scale: \nPrecision = ", fp, " | Recall = ", fr, " | F1-Score = ", ff1)

    

main()