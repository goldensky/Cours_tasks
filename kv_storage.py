import tempfile
import os
import argparse
import json





def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("--key", "-k", 
                    help='display a key in str for storage')
    parser.add_argument("--val",
                    help='display a value in str for storage')
    args = parser.parse_args()
    key = args.key
    val = args.val
    return key, val
    


k, v = create_parser()

storage_path = os.path.join(tempfile.gettempdir(), 'storage100.data')


if not os.path.exists(storage_path):
    os.makedirs(storage_path)
    #print(storage_path)

    
filename = os.path.join(storage_path, 'my_file.json')


#print('exists = ', os.path.exists(filename))

#print('isfile = ', os.path.isfile(filename))
#print('isdir = ', os.path.isdir(filename))




def to_storage_data():
    try:
        with open(filename, 'r') as f:
            old_content = json.load(f)
            #print(old_content)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        old_content = {}
    except:
        old_content = {}
        

    if str(k) in old_content:
        old_content[k].append(str(v))
    else:
        old_content[k] = [v]


    with open(filename, 'w') as f:
        json.dump(old_content, f)



       
        
def from_storage_data():
    try:
        with open(filename) as f:
            old_content = json.load(f)
            rez = old_content.get(k, None)
            if rez is not None:
                print(', '.join(rez))
            else:
                print(None)
    except FileNotFoundError as err:
        print( None)
        


if v is None:
    from_storage_data()
else:
    to_storage_data()










        

