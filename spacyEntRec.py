import re
import spacy
import AnalyzeDatasets

if __name__ == '__main__':
    #Fetch data from datasets
    input = AnalyzeDatasets.AnalyzeDatasets
    #Load spaCy NLP library and statistical models
    nlp = spacy.load("en_core_web_sm")

    #Initialize data string list
    data = []
    #This for loop appends any element found on csv datasets onto a data string list
    for row in input.frame.values:
        data.append(re.sub(r'\b\d+(?:\.\d+)?\s+', '', str(row)))

    #spaCy pipeline for identifying entities through data string list
    for doc in nlp.pipe(data, disable=["tagger", "parser"]):
        #Print any entity that has the ORG tag. ORG stands for Organization
        for ent in doc.ents:
            if ent.label_ =="ORG":
                print(ent.text, ent.label_)

    print('End of DetectEntities\n')
