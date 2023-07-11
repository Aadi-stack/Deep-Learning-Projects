import pickle

# Load the model
with open('neural.sav', 'rb') as file:
    model = pickle.load(file)

# Check the pickle protocol version
pickle_protocol = model.__getstate__()['pickle_protocol']
print(f"The pickle protocol version used for the model is: {pickle_protocol}")
