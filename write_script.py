from disq import Disque


def write_msgs():
    client = Disque()
    for i in range(1000):
        client.addjob('q', 'f%d' % i, retry_secs=1)

if __name__ == '__main__':
    write_msgs()
