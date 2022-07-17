from config import config
import redis,json,collections,requests
from connection import loadconnection



def readthroughcache():
    redis_client = loadconnection.setredisconnection()
    session = loadconnection.setcassandraconnection()
    print("Reading data simply..")
    rows = session.execute(query=config.app_config.CASSANDRA_QUERY)


    objects_list = []
    for row in rows:
        print(row)
        d = collections.OrderedDict()
        d["articleid"] = row[0]
        d["headline"] = row[1]
        d["newscategory"] = row[2]
        d["newssubcategory"] = row[3]
        d["numofhits"] = row[4]
        d["newspublishedtime"] = str(row[5])

        objects_list.append(d)

    jsonobject = json.dumps(objects_list)
    finaljsonobject = jsonobject.sort(key=lambda x: x["numofhits"])
    redis_client.set("news", finaljsonobject)

    return ("cache reloaded")
