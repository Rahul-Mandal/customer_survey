import pika, json

def publish_message(message):
    params = pika.URLParameters('amqp://guest:guest@rabbit-server1:5672/%2F')
    connection = pika.BlockingConnection(params)
    print('connec', connection)
    channel = connection.channel()
    channel.queue_declare("mq_queue")
    data = {
        "email": "rahul@gmail.com",
        "message": 'Hi this message is from Rahul'
    }
    channel.basic_publish(exchange='', routing_key='my_queue', body=json.dumps(data))
                          #body=message)
    