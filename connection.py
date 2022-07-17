from config import config
import redis
from cassandra.cluster import Cluster

class loadconnection:

    def setredisconnection(redisconnection):
        redis_client = redis.Redis(host=config.app_config.REDIS_HOST, port=config.app_config.REDIS_PORT, db=0)
        return redis_client

    def setcassandraconnection(cassandraconnection):
        cluster = Cluster(config.app_config.CASSANDRA_HOST, port=config.app_config.CASSANDRA_PORT)
        session = cluster.connect(keyspace=config.app_config.KEY_SPACE)
        return session

