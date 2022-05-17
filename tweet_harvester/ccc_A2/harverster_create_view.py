import couchdb
import logging

def createView( dbConn, designDoc, viewName, mapFunction, reduceFunction ):
    data = {
            "_id": f"_design/{designDoc}",
            "views": {
                viewName: {
                    "map": mapFunction,
                    "reduce": reduceFunction
                    }
            },
            "language": "javascript",
            "options": {"partitioned": False }
            }
    logging.info( f"creating view {designDoc}/{viewName}" )
    dbConn.save( data )

couch = couchdb.Server("http://admin:admin@172.26.131.153:5984")
db_mel = couch["mel_tweets"]
db_syd = couch["syd_tweets"]
db_bne = couch["bne_tweets"]

map_mel = '''function (doc) {
    if (doc.tweet.full_text.includes("network") || doc.tweet.full_text.includes("Network") || doc.tweet.full_text.includes("connectivity") || doc.tweet.full_text.includes("Connectivity") || doc.tweet.full_text.includes("affordablehousing") || doc.tweet.full_text.includes("affordable housing") || doc.tweet.full_text.includes("commuting") || doc.tweet.full_text.includes("Commuting") || doc.tweet.full_text.includes("connectedness") || doc.tweet.full_text.includes("neighbor") || doc.tweet.full_text.includes("social involvement") || doc.tweet.full_text.includes("socialinvolvement")) {
      emit("social connectedness Melbourne", {text:doc.tweet.full_text});
  }
}
'''

map_syd = '''function (doc) {
    if (doc.tweet.full_text.includes("network") || doc.tweet.full_text.includes("Network") || doc.tweet.full_text.includes("connectivity") || doc.tweet.full_text.includes("Connectivity") || doc.tweet.full_text.includes("affordablehousing") || doc.tweet.full_text.includes("affordable housing") || doc.tweet.full_text.includes("commuting") || doc.tweet.full_text.includes("Commuting") || doc.tweet.full_text.includes("connectedness") || doc.tweet.full_text.includes("neighbor") || doc.tweet.full_text.includes("social involvement") || doc.tweet.full_text.includes("socialinvolvement")) {
      emit("social connectedness Sydney", {text:doc.tweet.full_text});
  }
}
'''

map_bne = '''function (doc) {
    if (doc.tweet.full_text.includes("network") || doc.tweet.full_text.includes("Network") || doc.tweet.full_text.includes("connectivity") || doc.tweet.full_text.includes("Connectivity") || doc.tweet.full_text.includes("affordablehousing") || doc.tweet.full_text.includes("affordable housing") || doc.tweet.full_text.includes("commuting") || doc.tweet.full_text.includes("Commuting") || doc.tweet.full_text.includes("connectedness") || doc.tweet.full_text.includes("neighbor") || doc.tweet.full_text.includes("social involvement") || doc.tweet.full_text.includes("socialinvolvement")) {
      emit("social connectedness Brisbane", {text:doc.tweet.full_text});
  }
}
'''


reduceFunction = '''function(keys, values, rereduce) {
  if (rereduce) {
    return sum(values);
  } else {
    return values.length;
  }
}'''

if db_mel.__contains__('_design/social_connectedness_analysis'):
    db_mel.__delitem__('_design/social_connectedness_analysis')
createView( db_mel, "social_connectedness_analysis", "social_connectedness", map_mel, reduceFunction )

if db_syd.__contains__('_design/social_connectedness_analysis'):
    db_syd.__delitem__('_design/social_connectedness_analysis')
createView( db_syd, "social_connectedness_analysis", "social_connectedness", map_syd, reduceFunction )

if db_bne.__contains__('_design/social_connectedness_analysis'):
    db_bne.__delitem__('_design/social_connectedness_analysis')
createView( db_bne, "social_connectedness_analysis", "social_connectedness", map_bne, reduceFunction )


