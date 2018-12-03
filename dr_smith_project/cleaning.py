import pandas as pd






df = pd.read_csv("../../cleaned-data.csv")
unique_biodf_states = df.dropna(subset=["BIOGUIDE_ID"])
unique_biodf_states = unique_biodf_states.groupby(["YEAR", "BIOGUIDE_ID", "CATEGORY"])["AMOUNT"].sum().reset_index()
print(unique_biodf_states.head())





legiss = pd.read_csv("../../legislators_updated.csv")

def find_state(row):
    bio = row.BIOGUIDE_ID
    state = legiss.loc[legiss.bioguide_id == bio, "state"].values
    return str(state)[2:4]

unique_biodf_states["state"] = unique_biodf_states.apply(lambda row: find_state(row), axis=1)
unique_biodf_states = unique_biodf_states.loc[unique_biodf_states.state != "", :]

print (1)
def find_party(row):
    bio = row.BIOGUIDE_ID
    party = legiss.loc[legiss.bioguide_id == bio, "party"].values
    return str(party)[2:3]

unique_biodf_states["party"] = unique_biodf_states.apply(lambda row: find_party(row), axis=1)
unique_biodf_states = unique_biodf_states.loc[unique_biodf_states.party != "", :]
print(2)
def find_gender(row):
    bio = row.BIOGUIDE_ID
    party = legiss.loc[legiss.bioguide_id == bio, "gender"].values
    return str(party)[2:3]

unique_biodf_states["gender"] = unique_biodf_states.apply(lambda row: find_gender(row), axis=1)
unique_biodf_states = unique_biodf_states.loc[unique_biodf_states.party != "", :]

unique_biodf_states.loc[unique_biodf_states.state =="LA", "state"] = "LS"

unique_biodf_states.to_csv("../../cl.csv")
