from config import config
from flask import jsonify,make_response
from cassandra.cluster import Cluster
import redis,json,collections

class cassandraconnector:

    def buildresponsefromcassandra(N):
        redis_client = redis.Redis(host=config.app_config.REDIS_HOST, port=config.app_config.REDIS_PORT, db=0)
        responsefromredis=redis_client.get("news")
        # Limit the number of response here
        strresponse =(responsefromredis.decode("utf-8"))
        listresponse=list(eval(strresponse))
        finallistresponse=listresponse[0:N]
        return make_response((jsonify({'success': True, 'results': finallistresponse}), 200))
