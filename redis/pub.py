import sys

from faker import Faker

import redis

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)
faker = Faker('zh_CN')

if __name__ == '__main__':
    channel = sys.argv[1]

    while True:
        name = faker.name()
        message = input(u'Enter a message: '.encode('gbk'))
        if message.lower() == 'exit':
            break
        message = u'{name}: {message}'.format(**locals())

        r.publish(channel, message)
