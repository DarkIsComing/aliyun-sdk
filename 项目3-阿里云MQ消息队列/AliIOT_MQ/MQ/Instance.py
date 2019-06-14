from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_producer import *
from mq_http_sdk.mq_client import *
mq_client=MQClient("http://MQ_INST_1082287336727131_BaUeGeKg.cn-shanghai.mq-internal.aliyuncs.com:8080","LTAI4pGsbvGS61UN","S3AQwGGqdx2w6wdzVCfoJrFVgs3aLN")
#所属的 Topic
topic_name="My_MQ"
instance_id="MQ_INST_1082287336727131_BaUeGeKg"
producer = mq_client.get_producer(instance_id,topic_name)

msg_count = 100
print("%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count))
try:
    for i in range(msg_count):
        msg_body = "I am test message %s." % i
        msg = TopicMessage(
        	# 消息内容
        	"I am test message %s." % i, 
        	# 消息标签
        	""
        )
        re_msg = producer.publish_message(msg)
        print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5))
        time.sleep(1)
except MQExceptionBase as e:
    if e.type == "TopicNotExist":
        print("Topic not exist, please create it.")
        sys.exit(1)
    print("Publish Message Fail. Exception:%s" % e)
# #实例管理
# class Instance():
#     def __init__(self):
#         pass
#     #获取实例基本信息
#     def OnsInstanceBaseInfo(self,InstanceId,PreventCache):
#         '''
#         InstanceId  实例 ID
#         PreventCache  用于 CSRF 校验，设置为系统当前时间即可
#         '''




# if __name__=='__main__':
#     regionId='mq-internet-access'
#     accessKey='LTAI4pGsbvGS61UN'
#     secretKey='S3AQwGGqdx2w6wdzVCfoJrFVgs3aLN'