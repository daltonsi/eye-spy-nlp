####################
# By- Shreya Kapoor
####################

import pandas as pd
import requests

# API key
api_key = 'debbf5b1-4c57-4b5c-864b-8b67c947ab78'

# read in the disease_names file
disease_df = pd.read_csv('disease_names')

# create a new empty column for the CUI codes
disease_df['CUI'] = ''

# iterate through the rows of the dataframe and call the API to get the CUI code
for index, row in disease_df.iterrows():
    disease_name = row['Disease_name']
    url =  f'https://uts-ws.nlm.nih.gov/rest/search/current?string={disease_name}&apiKey={api_key}'
    # make the API call and retrieve the JSON response
    response = requests.get(url).json()
    # extract the CUI code from the response
    try:
        cui = response['result']['results'][0]['ui']
    except:
        cui = ''
    # update the corresponding row in the dataframe
    disease_df.at[index, 'CUI'] = cui

# write the dataframe to a csv file
disease_df.to_csv('disease_names_with_CUI', index=False)


