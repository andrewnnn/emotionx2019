import json
import pandas as pd

def to_df(file):
    if file:
        with open(file, 'r') as f:
            datastore = json.load(f)    
    
    utters = []
    for idx, convo in enumerate(datastore):
        for i in range(len(convo)):
            # for each convo, extract each 3 turn utterance | i - 1 | utterance | i + 1 |
            # Each utterance has the context before and after
            utter_context = []

            if (i - 1) >= 0:
                utter_context.append(convo[i-1])
            else:
                utter_context.append(None)

            utter_context.append(convo[i])

            if (i + 1) < len(convo):
                utter_context.append(convo[i+1])
            else:
                utter_context.append(None)

            utter_context.append(idx) # save convo id

            utters.append(utter_context)
    
    # Convert to pandas initialise format
    utters2 = []
    for u in utters:
        d = {}
        if u[0] != None:
            d["utterance1"] = u[0]["utterance"]
            if "emotion" in u[0]:
                d["emotion1"] = u[0]["emotion"]
            if "utterance_de" in u[0]:
                d["utterance1_de"] = u[0]["utterance_de"]
                d["utterance1_fr"] = u[0]["utterance_fr"]
                d["utterance1_it"] = u[0]["utterance_it"]

        d["utterance2"] = u[1]["utterance"]
        if "emotion" in u[1]:
            d["emotion2"] = u[1]["emotion"]
        if "utterance_de" in u[1]:
            d["utterance2_de"] = u[1]["utterance_de"]
            d["utterance2_fr"] = u[1]["utterance_fr"]
            d["utterance2_it"] = u[1]["utterance_it"]

        if u[2] != None:    
            d["utterance3"] = u[2]["utterance"]
            if "emotion" in u[2]:
                d["emotion3"] = u[2]["emotion"]
            if "utterance_de" in u[2]:
                d["utterance3_de"] = u[2]["utterance_de"]
                d["utterance3_fr"] = u[2]["utterance_fr"]
                d["utterance3_it"] = u[2]["utterance_it"]


        d["convoId"] = u[3]
        if "annotation" in u[1]:
            d["annotation"] = u[1]["annotation"]

        utters2.append(d)  
    
    df = pd.DataFrame(utters2)
    return df