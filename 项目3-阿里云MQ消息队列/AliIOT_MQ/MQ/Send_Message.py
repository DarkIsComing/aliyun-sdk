from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_producer import *
from mq_http_sdk.mq_client import *

#初始化 client
mq_client = MQClient(
    #设置HTTP接入域名（此处以公共云生产环境为例）
    "${HTTP_ENDPOINT}",
    #AccessKey 阿里云身份验证，在阿里云服务器管理控制台创建
    "${ACCESS_KEY}",
    #SecretKey 阿里云身份验证，在阿里云服务器管理控制台创建
    "${SECRET_KEY}"
	)
#所属的 Topic
topic_name = "${TOPIC}"
#Topic所属实例ID，默认实例为空None
instance_id = "${INSTANCE_ID}"

producer = mq_client.get_producer(instance_id, topic_name)

# 循环发布多条消息
msg_count = 100
print "%sPublish Message To %s\nTopicName:%s\nMessageCount:%s\n" % (10 * "=", 10 * "=", topic_name, msg_count)

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
        print "Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5)
        time.sleep(1)
except MQExceptionBase, e:
    if e.type == "TopicNotExist":
        print "Topic not exist, please create it."
        sys.exit(1)
    print "Publish Message Fail. Exception:%s" % e