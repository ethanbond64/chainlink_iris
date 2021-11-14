import datetime
import random
import pickle
import os

PERIOD_SIZE = (2**25)
EPOCH = datetime.datetime.utcfromtimestamp(0)
# event_datetime is field on event record in db
# entry mod is the numeric value of the identifier
def get_entry_timestamp(event_datetime,entry_mod):
    
    event_start = datetime_to_seconds(event_datetime)

    periods_on_start = event_start // PERIOD_SIZE

    remainder_on_start = event_start % PERIOD_SIZE

    if (entry_mod < remainder_on_start):
        periods_on_start += 1

    entry_timestamp = datetime.fromtimestamp(periods_on_start*PERIOD_SIZE + entry_mod)

    return entry_timestamp

def datetime_to_seconds(dt):
    return (dt - EPOCH).total_seconds()


# to be run manually
def generate_time_id_map():
    
    # create dict of random int to ordered int
    int_list = [i for i in range(PERIOD_SIZE)]
    random.shuffle(int_list)

    # save as pkl file in time_id_maps dir
    file_path = os.path.dirname(__file__) 
    abs_file_path = os.path.join(file_path, "/time_id_maps/time_id_map_1.pkl")

    with open(abs_file_path,'wb') as f:
        pickle.dump(int_list, f, protocol=pickle.HIGHEST_PROTOCOL)

    