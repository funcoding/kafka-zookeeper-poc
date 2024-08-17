from confluent_kafka import Producer
from time import sleep
from datetime import datetime

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

if __name__ == '__main__':
    try:
        p = Producer({'bootstrap.servers': '127.0.0.1:9092', "security.protocol": "PLAINTEXT"})
        
        for data in range(1,5):
            
            # Trigger any available delivery report callbacks from previous produce() calls
            p.poll(0)

            sleep(1)

            # Asynchronously produce a message. The delivery report callback will
            # be triggered from the call to poll() above, or flush() below, when the
            # message has been successfully delivered or failed permanently.
            p.produce('mytopic', "Message: {0}, time:{1}".format(data, datetime.now()), callback=delivery_report)

        # Wait for any outstanding messages to be delivered and delivery report
        # callbacks to be triggered.
        p.flush()

    except Exception as e:
        print(e)
        exit(0)
    finally:
        pass
