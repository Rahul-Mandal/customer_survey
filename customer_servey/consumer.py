import pika, json

def email_sender(mes):
    email = mes.get('email')
    message = mes.get('mes')
    print(email,message)

def callback(ch, method, properties, body):
    print(ch, method, properties, body)
    mes = body.decode()
    print(mes)
    email_sender(mes)
    params = pika.URLParameters('amqp://guest:guest@rabbit-server1:5672/%2F')
    connection = pika.BlockingConnection(params)
    print('connec', connection)
    channel = connection.channel()
    channel.queue_declare("mq_queue")
    channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
    print('consumer ready to consume rabitmq')
    channel.start_consuming()