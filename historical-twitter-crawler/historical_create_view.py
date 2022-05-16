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
db = couch["historical_tweets"]

map_walking_cyclying = '''function (doc) {
  if (doc.tweet.doc.geo) {
    if (doc.tweet.doc.text.includes("walk") || doc.tweet.doc.text.includes("Walk") || doc.tweet.doc.text.includes("WALK") || doc.tweet.doc.text.includes("cycling") || doc.tweet.doc.text.includes("bicycle") || doc.tweet.doc.text.includes("Cycling") || doc.tweet.doc.text.includes("Bicycle")) {
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9573 && doc.tweet.doc.geo.coordinates[1] < 144.9757 && doc.tweet.doc.geo.coordinates[0] >= -37.8079 && doc.tweet.doc.geo.coordinates[0] < -37.7923) {
        emit("Carlton", {text:doc.tweet.doc.text})
     }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9315 && doc.tweet.doc.geo.coordinates[1] < 144.9560 && doc.tweet.doc.geo.coordinates[0] >= -37.8253 && doc.tweet.doc.geo.coordinates[0] < -37.8095) {
        emit("Docklands", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9674 && doc.tweet.doc.geo.coordinates[1] < 144.9914 && doc.tweet.doc.geo.coordinates[0] >= -37.8297 && doc.tweet.doc.geo.coordinates[0] < -37.8077) {
        emit("East Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9027 && doc.tweet.doc.geo.coordinates[1] < 144.9229 && doc.tweet.doc.geo.coordinates[0] >= -37.7952 && doc.tweet.doc.geo.coordinates[0] < -37.7794) {
        emit("Flemington Racecourse", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9129 && doc.tweet.doc.geo.coordinates[1] < 144.9378 && doc.tweet.doc.geo.coordinates[0] >= -37.8023 && doc.tweet.doc.geo.coordinates[0] < -37.7874) {
        emit("Kensington (Vic.)", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9514 && doc.tweet.doc.geo.coordinates[1] < 144.9749 && doc.tweet.doc.geo.coordinates[0] >= -37.8231 && doc.tweet.doc.geo.coordinates[0] < -37.8059) {
        emit("Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9357 && doc.tweet.doc.geo.coordinates[1] < 144.9595 && doc.tweet.doc.geo.coordinates[0] >= -37.8135 && doc.tweet.doc.geo.coordinates[0] < -37.7876) {
        emit("North Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9371 && doc.tweet.doc.geo.coordinates[1] < 144.9650 && doc.tweet.doc.geo.coordinates[0] >= -37.8016 && doc.tweet.doc.geo.coordinates[0] < -37.7754) {
        emit("Parkville", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9377 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8343 && doc.tweet.doc.geo.coordinates[0] < -37.8192) {
        emit("Southbank", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9723 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8507 && doc.tweet.doc.geo.coordinates[0] < -37.8283) {
        emit("South Yarra - West", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9055 && doc.tweet.doc.geo.coordinates[1] < 144.9460 && doc.tweet.doc.geo.coordinates[0] >= -37.8233 && doc.tweet.doc.geo.coordinates[0] < -37.7982) {
        emit("West Melbourne", {text:doc.tweet.doc.text})
      }
    }
  }
}'''

map_traffic = '''function (doc) {
  if (doc.tweet.doc.geo) {
    if (doc.tweet.doc.text.includes("traffic") || doc.tweet.doc.text.includes("Traffic") || doc.tweet.doc.text.includes("TRAFFIC")) {
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9573 && doc.tweet.doc.geo.coordinates[1] < 144.9757 && doc.tweet.doc.geo.coordinates[0] >= -37.8079 && doc.tweet.doc.geo.coordinates[0] < -37.7923) {
        emit("Carlton", {text:doc.tweet.doc.text})
     }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9315 && doc.tweet.doc.geo.coordinates[1] < 144.9560 && doc.tweet.doc.geo.coordinates[0] >= -37.8253 && doc.tweet.doc.geo.coordinates[0] < -37.8095) {
        emit("Docklands", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9674 && doc.tweet.doc.geo.coordinates[1] < 144.9914 && doc.tweet.doc.geo.coordinates[0] >= -37.8297 && doc.tweet.doc.geo.coordinates[0] < -37.8077) {
        emit("East Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9027 && doc.tweet.doc.geo.coordinates[1] < 144.9229 && doc.tweet.doc.geo.coordinates[0] >= -37.7952 && doc.tweet.doc.geo.coordinates[0] < -37.7794) {
        emit("Flemington Racecourse", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9129 && doc.tweet.doc.geo.coordinates[1] < 144.9378 && doc.tweet.doc.geo.coordinates[0] >= -37.8023 && doc.tweet.doc.geo.coordinates[0] < -37.7874) {
        emit("Kensington (Vic.)", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9514 && doc.tweet.doc.geo.coordinates[1] < 144.9749 && doc.tweet.doc.geo.coordinates[0] >= -37.8231 && doc.tweet.doc.geo.coordinates[0] < -37.8059) {
        emit("Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9357 && doc.tweet.doc.geo.coordinates[1] < 144.9595 && doc.tweet.doc.geo.coordinates[0] >= -37.8135 && doc.tweet.doc.geo.coordinates[0] < -37.7876) {
        emit("North Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9371 && doc.tweet.doc.geo.coordinates[1] < 144.9650 && doc.tweet.doc.geo.coordinates[0] >= -37.8016 && doc.tweet.doc.geo.coordinates[0] < -37.7754) {
        emit("Parkville", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9377 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8343 && doc.tweet.doc.geo.coordinates[0] < -37.8192) {
        emit("Southbank", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9723 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8507 && doc.tweet.doc.geo.coordinates[0] < -37.8283) {
        emit("South Yarra - West", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9055 && doc.tweet.doc.geo.coordinates[1] < 144.9460 && doc.tweet.doc.geo.coordinates[0] >= -37.8233 && doc.tweet.doc.geo.coordinates[0] < -37.7982) {
        emit("West Melbourne", {text:doc.tweet.doc.text})
      }
    }
  }
}'''

map_publictransport = '''function (doc) {
  if (doc.tweet.doc.geo) {
    if (doc.tweet.doc.text.includes("public transport") || doc.tweet.doc.text.includes("Public transport") || doc.tweet.doc.text.includes("Public Transport") || doc.tweet.doc.text.includes("PUBLIC TRANSPORT") || doc.tweet.doc.text.includes("publictransport") || doc.tweet.doc.text.includes("urban mobility") || doc.tweet.doc.text.includes("urbanmobility")) {
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9573 && doc.tweet.doc.geo.coordinates[1] < 144.9757 && doc.tweet.doc.geo.coordinates[0] >= -37.8079 && doc.tweet.doc.geo.coordinates[0] < -37.7923) {
        emit("Carlton", {text:doc.tweet.doc.text})
     }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9315 && doc.tweet.doc.geo.coordinates[1] < 144.9560 && doc.tweet.doc.geo.coordinates[0] >= -37.8253 && doc.tweet.doc.geo.coordinates[0] < -37.8095) {
        emit("Docklands", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9674 && doc.tweet.doc.geo.coordinates[1] < 144.9914 && doc.tweet.doc.geo.coordinates[0] >= -37.8297 && doc.tweet.doc.geo.coordinates[0] < -37.8077) {
        emit("East Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9027 && doc.tweet.doc.geo.coordinates[1] < 144.9229 && doc.tweet.doc.geo.coordinates[0] >= -37.7952 && doc.tweet.doc.geo.coordinates[0] < -37.7794) {
        emit("Flemington Racecourse", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9129 && doc.tweet.doc.geo.coordinates[1] < 144.9378 && doc.tweet.doc.geo.coordinates[0] >= -37.8023 && doc.tweet.doc.geo.coordinates[0] < -37.7874) {
        emit("Kensington (Vic.)", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9514 && doc.tweet.doc.geo.coordinates[1] < 144.9749 && doc.tweet.doc.geo.coordinates[0] >= -37.8231 && doc.tweet.doc.geo.coordinates[0] < -37.8059) {
        emit("Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9357 && doc.tweet.doc.geo.coordinates[1] < 144.9595 && doc.tweet.doc.geo.coordinates[0] >= -37.8135 && doc.tweet.doc.geo.coordinates[0] < -37.7876) {
        emit("North Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9371 && doc.tweet.doc.geo.coordinates[1] < 144.9650 && doc.tweet.doc.geo.coordinates[0] >= -37.8016 && doc.tweet.doc.geo.coordinates[0] < -37.7754) {
        emit("Parkville", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9377 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8343 && doc.tweet.doc.geo.coordinates[0] < -37.8192) {
        emit("Southbank", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9723 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8507 && doc.tweet.doc.geo.coordinates[0] < -37.8283) {
        emit("South Yarra - West", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9055 && doc.tweet.doc.geo.coordinates[1] < 144.9460 && doc.tweet.doc.geo.coordinates[0] >= -37.8233 && doc.tweet.doc.geo.coordinates[0] < -37.7982) {
        emit("West Melbourne", {text:doc.tweet.doc.text})
      }
    }
  }
}'''

map_driverlessvehicles = '''function (doc) {
  if (doc.tweet.doc.geo) {
    if (doc.tweet.doc.text.includes("driverless") || doc.tweet.doc.text.includes("Driverless") || doc.tweet.doc.text.includes("DRIVERLESS")) {
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9573 && doc.tweet.doc.geo.coordinates[1] < 144.9757 && doc.tweet.doc.geo.coordinates[0] >= -37.8079 && doc.tweet.doc.geo.coordinates[0] < -37.7923) {
        emit("Carlton", {text:doc.tweet.doc.text})
     }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9315 && doc.tweet.doc.geo.coordinates[1] < 144.9560 && doc.tweet.doc.geo.coordinates[0] >= -37.8253 && doc.tweet.doc.geo.coordinates[0] < -37.8095) {
        emit("Docklands", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9674 && doc.tweet.doc.geo.coordinates[1] < 144.9914 && doc.tweet.doc.geo.coordinates[0] >= -37.8297 && doc.tweet.doc.geo.coordinates[0] < -37.8077) {
        emit("East Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9027 && doc.tweet.doc.geo.coordinates[1] < 144.9229 && doc.tweet.doc.geo.coordinates[0] >= -37.7952 && doc.tweet.doc.geo.coordinates[0] < -37.7794) {
        emit("Flemington Racecourse", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9129 && doc.tweet.doc.geo.coordinates[1] < 144.9378 && doc.tweet.doc.geo.coordinates[0] >= -37.8023 && doc.tweet.doc.geo.coordinates[0] < -37.7874) {
        emit("Kensington (Vic.)", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9514 && doc.tweet.doc.geo.coordinates[1] < 144.9749 && doc.tweet.doc.geo.coordinates[0] >= -37.8231 && doc.tweet.doc.geo.coordinates[0] < -37.8059) {
        emit("Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9357 && doc.tweet.doc.geo.coordinates[1] < 144.9595 && doc.tweet.doc.geo.coordinates[0] >= -37.8135 && doc.tweet.doc.geo.coordinates[0] < -37.7876) {
        emit("North Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9371 && doc.tweet.doc.geo.coordinates[1] < 144.9650 && doc.tweet.doc.geo.coordinates[0] >= -37.8016 && doc.tweet.doc.geo.coordinates[0] < -37.7754) {
        emit("Parkville", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9377 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8343 && doc.tweet.doc.geo.coordinates[0] < -37.8192) {
        emit("Southbank", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9723 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8507 && doc.tweet.doc.geo.coordinates[0] < -37.8283) {
        emit("South Yarra - West", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9055 && doc.tweet.doc.geo.coordinates[1] < 144.9460 && doc.tweet.doc.geo.coordinates[0] >= -37.8233 && doc.tweet.doc.geo.coordinates[0] < -37.7982) {
        emit("West Melbourne", {text:doc.tweet.doc.text})
      }
    }
  }
}'''

map_airport = '''function (doc) {
  if (doc.tweet.doc.geo) {
    if (doc.tweet.doc.text.includes("airport") || doc.tweet.doc.text.includes("Airport") || doc.tweet.doc.text.includes("AIRPORT") || doc.tweet.doc.text.includes("melbourneairport") || doc.tweet.doc.text.includes("Melbourneairport")){
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9573 && doc.tweet.doc.geo.coordinates[1] < 144.9757 && doc.tweet.doc.geo.coordinates[0] >= -37.8079 && doc.tweet.doc.geo.coordinates[0] < -37.7923) {
        emit("Carlton", {text:doc.tweet.doc.text});
     }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9315 && doc.tweet.doc.geo.coordinates[1] < 144.9560 && doc.tweet.doc.geo.coordinates[0] >= -37.8253 && doc.tweet.doc.geo.coordinates[0] < -37.8095) {
        emit("Docklands", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9674 && doc.tweet.doc.geo.coordinates[1] < 144.9914 && doc.tweet.doc.geo.coordinates[0] >= -37.8297 && doc.tweet.doc.geo.coordinates[0] < -37.8077) {
        emit("East Melbourne", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9027 && doc.tweet.doc.geo.coordinates[1] < 144.9229 && doc.tweet.doc.geo.coordinates[0] >= -37.7952 && doc.tweet.doc.geo.coordinates[0] < -37.7794) {
        emit("Flemington Racecourse", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9129 && doc.tweet.doc.geo.coordinates[1] < 144.9378 && doc.tweet.doc.geo.coordinates[0] >= -37.8023 && doc.tweet.doc.geo.coordinates[0] < -37.7874) {
        emit("Kensington (Vic.)", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9514 && doc.tweet.doc.geo.coordinates[1] < 144.9749 && doc.tweet.doc.geo.coordinates[0] >= -37.8231 && doc.tweet.doc.geo.coordinates[0] < -37.8059) {
        emit("Melbourne", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9357 && doc.tweet.doc.geo.coordinates[1] < 144.9595 && doc.tweet.doc.geo.coordinates[0] >= -37.8135 && doc.tweet.doc.geo.coordinates[0] < -37.7876) {
        emit("North Melbourne", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9371 && doc.tweet.doc.geo.coordinates[1] < 144.9650 && doc.tweet.doc.geo.coordinates[0] >= -37.8016 && doc.tweet.doc.geo.coordinates[0] < -37.7754) {
        emit("Parkville", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9377 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8343 && doc.tweet.doc.geo.coordinates[0] < -37.8192) {
        emit("Southbank", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9723 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8507 && doc.tweet.doc.geo.coordinates[0] < -37.8283) {
        emit("South Yarra - West", {text:doc.tweet.doc.text});
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9055 && doc.tweet.doc.geo.coordinates[1] < 144.9460 && doc.tweet.doc.geo.coordinates[0] >= -37.8233 && doc.tweet.doc.geo.coordinates[0] < -37.7982) {
        emit("West Melbourne", {text:doc.tweet.doc.text});
      }
    }
  }
}'''

map_railways = '''function (doc) {
  if (doc.tweet.doc.geo) {
    if (doc.tweet.doc.text.includes("rail") || doc.tweet.doc.text.includes("Rail") || doc.tweet.doc.text.includes("RAIL") || doc.tweet.doc.text.includes("train") || doc.tweet.doc.text.includes("Train") || doc.tweet.doc.text.includes("TRAIN")) {
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9573 && doc.tweet.doc.geo.coordinates[1] < 144.9757 && doc.tweet.doc.geo.coordinates[0] >= -37.8079 && doc.tweet.doc.geo.coordinates[0] < -37.7923) {
        emit("Carlton", {text:doc.tweet.doc.text})
     }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9315 && doc.tweet.doc.geo.coordinates[1] < 144.9560 && doc.tweet.doc.geo.coordinates[0] >= -37.8253 && doc.tweet.doc.geo.coordinates[0] < -37.8095) {
        emit("Docklands", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9674 && doc.tweet.doc.geo.coordinates[1] < 144.9914 && doc.tweet.doc.geo.coordinates[0] >= -37.8297 && doc.tweet.doc.geo.coordinates[0] < -37.8077) {
        emit("East Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9027 && doc.tweet.doc.geo.coordinates[1] < 144.9229 && doc.tweet.doc.geo.coordinates[0] >= -37.7952 && doc.tweet.doc.geo.coordinates[0] < -37.7794) {
        emit("Flemington Racecourse", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9129 && doc.tweet.doc.geo.coordinates[1] < 144.9378 && doc.tweet.doc.geo.coordinates[0] >= -37.8023 && doc.tweet.doc.geo.coordinates[0] < -37.7874) {
        emit("Kensington (Vic.)", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9514 && doc.tweet.doc.geo.coordinates[1] < 144.9749 && doc.tweet.doc.geo.coordinates[0] >= -37.8231 && doc.tweet.doc.geo.coordinates[0] < -37.8059) {
        emit("Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9357 && doc.tweet.doc.geo.coordinates[1] < 144.9595 && doc.tweet.doc.geo.coordinates[0] >= -37.8135 && doc.tweet.doc.geo.coordinates[0] < -37.7876) {
        emit("North Melbourne", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9371 && doc.tweet.doc.geo.coordinates[1] < 144.9650 && doc.tweet.doc.geo.coordinates[0] >= -37.8016 && doc.tweet.doc.geo.coordinates[0] < -37.7754) {
        emit("Parkville", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9377 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8343 && doc.tweet.doc.geo.coordinates[0] < -37.8192) {
        emit("Southbank", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9723 && doc.tweet.doc.geo.coordinates[1] < 144.9879 && doc.tweet.doc.geo.coordinates[0] >= -37.8507 && doc.tweet.doc.geo.coordinates[0] < -37.8283) {
        emit("South Yarra - West", {text:doc.tweet.doc.text})
      }
      if (doc.tweet.doc.geo.coordinates[1] >= 144.9055 && doc.tweet.doc.geo.coordinates[1] < 144.9460 && doc.tweet.doc.geo.coordinates[0] >= -37.8233 && doc.tweet.doc.geo.coordinates[0] < -37.7982) {
        emit("West Melbourne", {text:doc.tweet.doc.text})
      }
    }
  }
}'''

reduceFunction = '''function(keys, values, rereduce) {
  if (rereduce) {
    return sum(values);
  } else {
    return values.length;
  }
}'''

if db.__contains__('_design/walking_cyclying_analysis'):
    db.__delitem__('_design/walking_cyclying_analysis')
createView( db, "walking_cyclying_analysis", "walking_cyclying", map_walking_cyclying, reduceFunction )

if db.__contains__('_design/traffic_analysis'):
    db.__delitem__('_design/traffic_analysis')
createView( db, "traffic_analysis", "traffic", map_traffic, reduceFunction )

if db.__contains__('_design/publictransport_analysis'):
    db.__delitem__('_design/publictransport_analysis')
createView( db, "publictransport_analysis", "publictransport", map_publictransport, reduceFunction )

if db.__contains__('_design/driverlessvehicles_analysis'):
    db.__delitem__('_design/driverlessvehicles_analysis')
createView( db, "driverlessvehicles_analysis", "driverlessvehicles", map_driverlessvehicles, reduceFunction )

if db.__contains__('_design/airport_analysis'):
    db.__delitem__('_design/airport_analysis')
createView( db, "airport_analysis", "airport", map_airport, reduceFunction )

if db.__contains__('_design/railways_analysis'):
    db.__delitem__('_design/railways_analysis')
createView( db, "railways_analysis", "railways", map_railways, reduceFunction )



