
from server.blueprints.main.models import Entry

# By single entry? Or include the query into this method
def get_confirmations(entry: Entry,event_id):

    # Define a tolerance for the auth timestamp,
    # +/- this number in seconds for how long after other device signatures 
    #  can send in the same data for it to be confirmed
    tolerance = 5

    # order by device signature, manually filter outside of query
    entries = Entry.query.filter(
                Entry.event_id==event_id,
                Entry.timestamp>=(entry.timestamp-tolerance),
                Entry.timestamp<=(entry.timestamp+tolerance),
                Entry.device_signature!=entry.device_signature
            ).order_by(Entry.device_signature).limit(10)
    

    confirmed_count = 0
    seen_signatures = []
    for ent in entries:
        if ent.device_signature not in seen_signatures:
            if ent.data == entry.data:
                confirmed_count += 1

            seen_signatures.append(ent.device_signature)

    return confirmed_count



