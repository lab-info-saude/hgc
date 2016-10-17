'''import pickle
def save_it_now(ar=None, avr=None, aar=None,c=None, file_name="data_1"):
    data = {"right":{"angles":ar, "angular velocities": avr,
                     "angular accelerations":aar, "classifier index":c}}
    f = open (file_name, "w")
    ndata = pickle.dumps(data)
    f.write(ndata)
    f.close()
    print "Saved to file"


def load_file(file_name="data_1"):
    f = open(file_name, "r")
    return pickle.loads(f.read())'''

import pickle
def save_it_now(Xc=None, file_name="data_1"):

    f = open (file_name, "w")
    ndata = pickle.dumps(Xc)
    f.write(ndata)
    f.close()
    print "Saved to file"


def load_file(file_name="data_1"):
    f = open(file_name, "r")
    return pickle.loads(f.read())
