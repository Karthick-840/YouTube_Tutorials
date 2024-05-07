import pickle

with open("data.pkl", "rb") as f:
    # Load the pickled data
    imported_data = pickle.load(f)
    
print(imported_data)