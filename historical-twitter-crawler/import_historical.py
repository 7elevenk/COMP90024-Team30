import couchdb
import json

couch = couchdb.Server("http://admin:admin@172.26.131.153:5984")
db = couch["historical_testset"]

with open("twitter-melb.json") as jsonfile:
    for row in jsonfile:
        if "total_rows" not in row:
            db_entry = json.loads(row[:-2])
            doc_id = db_entry["id"]
            if doc_id not in db:
                db[doc_id] = {"tweet": db_entry}
