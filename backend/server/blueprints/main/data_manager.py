
import datetime
from server.blueprints.main.models import Event, Entry, Event_Entry_Xref

from server.blueprints.main.time_handler import img_to_bin, get_entry_timestamp

def save_event_record(img, event: Event):

    # Check event is still valid
    if event.expiration < datetime.datetime.now() or event.start_time > datetime.datetime.now():
        return
    
    # get event data policy
    policy = event.dataPolicy

    # check for time auth
    auth_timestamp = None
    try:
        binary_timestamp = img_to_bin(img)
        auth_timestamp = get_entry_timestamp(event.start_time,int(binary_timestamp, 2))
    except:
        auth_timestamp = datetime.datetime.now()

    # Use data policy to get data
    generated_json = {"data":"fake"}

    # save an entry for the event
    entry = Entry(data=generated_json,timestamp=auth_timestamp).save()

    # save in the xref
    Event_Entry_Xref(entry_id=entry.id,event_id=event.id).save()
