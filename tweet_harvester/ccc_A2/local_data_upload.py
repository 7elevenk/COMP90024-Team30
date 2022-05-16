import json
import couchdb


# Access to own CouchDB
couch = couchdb.Server("http://admin:admin@172.26.134.181:5984")

# Point out the database

db_name = "mel_tweets"
if db_name in couch:
    db = couch[db_name]
else:
    db = couch.create(db_name)

count = 0

file_name = "tweets_cbd1.json"
with open(file_name) as file:
    for row in file:
        if row[0] != "[" and row[0] != "]":
            row = row.strip()
            tweet = json.dumps(row)
            db_entry = json.loads(tweet)
            # Find out the unique ID for each twitter
            doc_id = db_entry[55:74]
            #print(doc_id)

            # Handling with duplicate tweets
            if str(doc_id) not in db:
                db[str(doc_id)] = {"tweet": db_entry}
                print("loaded")
                count += 1


print(count)
