import spacy
import preprocessing

def main():
    #intialize data object
    data = preprocessing.ProcessedData()

    #Print data info
    data.dataInfo()

    #ONLY CALL THIS FUNCTION IF WE WANT TO RECREATE adjectiveList.txt
    #Get all the adjectives
    #adjList = getAllAdjectives(data.X_train)



#Takes in the training data
#Writes a list of all the discovered adjectives to adjectives.txt
def getAllAdjectives(xTrain):
    adjList = []
    nounList = []
    count = 0
    #Load spacy
    eng = spacy.load("en_core_web_sm")
    #iterate through the training data
    for sentence in xTrain.iteritems():
        #convert sentence to spacy object
        spacySentence = eng(sentence[1])
        #For word in spacy object
        for token in spacySentence:
            #If its a noun, we dont want it added as an adjective, so add it to nouns
            if (token.pos_ == "NOUN"):
                if (token.text not in nounList):
                    nounList.append(token.text)
            #If its and adjective and its not already in either the noun or adjective list, add it
            if (token.pos_ == "ADJ"):
                if (token.text not in adjList and token.text not in nounList):
                    adjList.append(token.text.lower())
        #This is for progress printing so I dont worry about it hangning
        count += 1
        if(count % 5000 == 0):
            print("Sentence " + str(count) + " completed")

    f = open("adjectiveList.txt", "w+", encoding="utf-8")
    for i in adjList:
        f.write(i)
        f.write(',')
    f.close()
    return adjList


main()