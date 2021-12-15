import re
import spacy


adjectives = []
def loadAdj():

    with open("adjectiveList.txt", "r", encoding="utf-8") as fs:

        for line in fs:

            cur = line.split(",")
            for adj in cur:

                if(adj not in adjectives):
                    adjectives.append(adj)  

    print("Total Unique Adjectives",len(adjectives))

#feature test sentence. first review in reviews.txt
tsen = "Stayed in a king suite for 11 nights and yes it cots us a bit but we were happy with the standard of room, the location and the friendliness of the staff. Our room was on the 20th floor overlooking Broadway and the madhouse of the Fairway Market. Room was quite with no noise evident from the hallway or adjoining rooms. It was great to be able to open windows when we craved fresh rather than heated air. The beds, including the fold out sofa bed, were comfortable and the rooms were cleaned well. Wi-fi access worked like a dream with only one connectivity issue on our first night and this was promptly responded to with a call from the service provider to ensure that all was well. The location close to the 72nd Street subway station is great and the complimentary umbrellas on the drizzly days were greatly appreciated. It is fabulous to have the kitchen with cooking facilities and the access to a whole range of fresh foods directly across the road at Fairway.This is the second time that members of the party have stayed at the Beacon and it will certainly be our hotel of choice for future visits."


#Features
def review_len(rvw):

    sen = re.split(" ", rvw)
    return len(sen)

#Returns number of adjectives and a list of the adjectives
def adj_count(rvw):

    adjs = 0
    adjList = []
    eng = spacy.load("en_core_web_sm")

    sens = re.split(" ", rvw)
    for word in sens:

        if(word in adjectives):
            spacyWord = eng(word)
            if(spacyWord[0].pos_ == "ADJ"):
                adjList.append(word)
                adjs += 1

    return adjs, adjList
    


if(__name__ == "__main__"):
    loadAdj()

    adjFound, adjList = adj_count(tsen)
    print("Sentence length: ",review_len(tsen))
    print("Adjectives found: ",adj_count(tsen))
    print(adjList)