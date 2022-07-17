from config import config
from DAL import cassandra_dal,rediscache_refresh
import connection

class commoncontroller:

    def validate(N)->bool:
        if N>config.app_config.NUMBER_OF_NEWS:
            return False
        elif not isinstance(N,int):
            return False
        else:
            return True

    def processrequest(N):
        response=cassandra_dal.cassandraconnector.buildresponsefromcassandra(N)
        return response

    def processredisrequest(app,timetolive):
        response=rediscache_refresh.redisconnector.redisrefreshcache(app,timetolive)
        return response





