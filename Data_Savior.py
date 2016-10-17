import pickle
def save_it_now(ar=None, avr=None, aar=None,v3dr=None, al=None, avl=None, aal=None,v3dl=None, file_name="data_1"):
    data = {"right":{"angles":ar, "angular velocities": avr,
                     "angular accelerations":aar, "3d velocities":v3dr}, "left":{"angles":al, "angular velocities": avl,
                     "angular accelerations":aal, "3d velocities":v3dl}}
    f = open (file_name, "w")
    ndata = pickle.dumps(data)
    f.write(ndata)
    f.close()
    print "Saved to file"

        
def load_file(file_name="data_1"):
    f = open(file_name, "r")
    return pickle.loads(f.read())

