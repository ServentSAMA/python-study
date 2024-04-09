import redis

class RedisPubSub(object):

    def __init__(self, channl):
        self.__conn = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        self.chan_sub = channl
    
    def pub(self, message):
        """
        在指定频道上发送信息
        :param message:
        """
        self.__conn.publish(self.chan_sub, message)
