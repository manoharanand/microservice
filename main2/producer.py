import pika, json
params = pika.URLParameters('amqps://slfsxtdl:sNjjIqtNGtcro4MQaV8zYsS0LliCy-XW@armadillo.rmq.cloudamqp.com/slfsxtdl')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body),properties=properties )