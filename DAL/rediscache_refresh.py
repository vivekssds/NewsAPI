from config import config
import redis,json,collections,requests

from flask import jsonify
from cassandra.cluster import Cluster

class redisconnector:
    def redisrefreshcache(app,timetolive):
        redis_client = redis.Redis(host=config.app_config.REDIS_HOST, port=config.app_config.REDIS_PORT, db=0)
        cluster = Cluster(config.app_config.CASSANDRA_HOST, port=config.app_config.CASSANDRA_PORT)
        session = cluster.connect(keyspace=config.app_config.KEY_SPACE)
        print("Reading data simply..")
        rows = session.execute(query=config.app_config.CASSANDRA_QUERY)

        # read through cache

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
        # products.sort(key=lambda x: x["brand"])
        j = jsonify(objects_list)
        redis_client.flushall()
        jsonobject=json.dumps(objects_list)
        finaljsonobject=jsonobject.sort(key=lambda x: x["numofhits"])
        redis_client.set("news", finaljsonobject)

        return ("cache reloaded")