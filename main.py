import re
import spacy
import AnalyzeDatasets

if __name__ == '__main__':
    input = AnalyzeDatasets.AnalyzeDatasets
    nlp = spacy.load("en_core_web_sm")

    data = []
    for row in input.frame.values:
        data.append(re.sub(r'\b\d+(?:\.\d+)?\s+', '', str(row)))

    #print(data)
    for doc in nlp.pipe(data, disable=["tagger", "parser"]):
        #Locations, Organizations, Priodutcts, GPE
        print([(ent.text, ent.label_) for ent in doc.ents])