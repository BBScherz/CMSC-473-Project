import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#Fields: X_train, X_dev, X_test, y_train, y_dev, y_test, data, rating_dist
class ProcessedData:
    def __init__(self):
        #Read in data
        self.data = pd.read_csv("review.csv")

        #Split the reviews (data to evaluate) from the ratings (labels)
        X = self.data["Review"]
        y = self.data["Rating"]
        
        #Split the data into a training and a test set; random_state=42 for consistency, split into 85% for training and dev, 15% for evaluation
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, shuffle=True, test_size=0.15, random_state=42)

        #Split the training set into a dev and training set. Test size is .18 because that splits the training into approximately 70% for training
        #15% for dev
        self.X_train, self.X_dev, self.y_train, self.y_dev = train_test_split(self.X_train, self.y_train, shuffle=True, test_size=0.18, random_state=24)

        #Calculate distribution of ratings in y_train data set
        self.rating_dist = [0, 0, 0, 0, 0]  #List of star rating counts
        #For each label in y_dist, add a count to rating_dist for the designated rating
        for y in self.y_train:
            self.rating_dist[y-1] += 1

    #This function prints information related to the data, such as its shape, entries, and pandas description.
    def dataInfo(self):
        # Print data shape
        print("Full data Shape: ", end = '')
        print(self.data.shape)

        # Show the first five rows
        print(self.data.head(5))

        #Check the count, types of the data we have, and memory usage
        self.data.info()

        #Show the distribution of the ratings labels
        self.data.describe()

        # Check if there is any na values in data
        self.data.isna().sum()

        #Print the shape of the training data we just split
        print("Training Data X Shape: ",end = '')
        print(self.X_train.shape)
        print("Training Data y Shape: ",end = '')
        print(self.y_train.shape)


    #This function shows a bar graph of the distribution of ratings (1-5) in the training data set
    def showRatingDist(self):
        #Plot the distribution of star ratings in the training data
        fig = plt.figure(figsize=(24,8))
        ax = fig.add_axes([0,0,1,1])
        rating_labels = ['1', '2', '3', '4', '5']
        ax.bar(rating_labels, self.rating_dist)

        plt.title('Distribution of Ratings in Training Data', fontsize=18)
        plt.xlabel('Star Rating', fontsize=16)
        plt.ylabel('Counts', fontsize=16)
        plt.show()

    def writeToTextFile(self):
        #Output all of the reviews in the training set into a file to see what the reviews look like
        with open("train_reviews.txt", 'w', encoding="utf-8") as sentence_file:
            for review in self.X_train:
                sentence_file.write(review + '\n')


    