import re
import boto3
import AnalyzeDatasets

qdata = {
    'commentid': id,
    'Text': "",
    'Score': 0,
    'BeginOffset': 0,
    'EndOffset': 0,
    'Type': "",
  }

#Start connection with boto3 (amazon comprehend)
comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
#Call AnalyzeDatasets class
input = AnalyzeDatasets.AnalyzeDatasets

print('Calling DetectEntities\n')

#Initiaize enData object list
enData = []

#Iterrate the values that frame object list has
for row in input.frame.values:
    #Detect entities using amazon comprehend of each row of frame object list
    enData = comprehend.detect_entities(Text=re.sub(r'\b\d+(?:\.\d+)?\s+', '', str(row)), LanguageCode='en')

    # entity data preparation and handling
    for entity in enData['Entities']:
        qdata['Type'] = entity['Type']
        qdata['Text'] = entity['Text']
        qdata['Score'] = entity['Score']
        qdata['BeginOffset'] = entity['BeginOffset']
        qdata['EndOffset'] = entity['EndOffset']

        #Entity keyword searching - print any detected entity which is type of ORGANIZATION
        if(qdata['Type'] == "ORGANIZATION"):
            print(qdata['Text'] + ' ' + qdata['Type'])

print('End of DetectEntities\n')
