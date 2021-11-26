from cv2 import imread, GaussianBlur, Canny, findContours, RETR_TREE, CHAIN_APPROX_SIMPLE
import datetime
import random
import pickle
import os

# PERIOD_SIZE = (2**25)
# EPOCH = datetime.datetime.utcfromtimestamp(0)
# # event_datetime is field on event record in db
# # entry mod is the numeric value of the identifier

# def get_entry_timestamp(event_datetime,entry_mod):
    
#     event_start = datetime_to_seconds(event_datetime)

#     periods_on_start = event_start // PERIOD_SIZE

#     remainder_on_start = event_start % PERIOD_SIZE

#     if (entry_mod < remainder_on_start):
#         periods_on_start += 1

#     entry_timestamp = datetime.fromtimestamp(periods_on_start*PERIOD_SIZE + entry_mod)

#     return entry_timestamp

# def datetime_to_seconds(dt):
#     return (dt - EPOCH).total_seconds()


# # to be run manually
# def generate_time_id_map():
    
#     # create dict of random int to ordered int
#     int_list = [i for i in range(PERIOD_SIZE)]
#     random.shuffle(int_list)

#     # save as pkl file in time_id_maps dir
#     file_path = os.path.dirname(__file__) 
#     abs_file_path = os.path.join(file_path, "/time_id_maps/time_id_map_1.pkl")

#     with open(abs_file_path,'wb') as f:
#         pickle.dump(int_list, f, protocol=pickle.HIGHEST_PROTOCOL)

# def img_to_bin(img):
#     # TODO make this not suck
#     blurred = GaussianBlur(img, (5, 5), 0) # Blur
#     canny = Canny(blurred, 30, 150) # Canny
#     contours, _ = findContours(canny,RETR_TREE,CHAIN_APPROX_SIMPLE)
#     contours = contours[0::len(contours)//25]
#     bin_rep = ""
#     for c in contours:
#         if img[c[0][0][1]+5][c[0][0][0]+5][0] != 255:
#             bin_rep += "1"
#         else:
#             bin_rep += "0"
#     bin_rep = bin_rep[::-1]
#     return bin_rep

    