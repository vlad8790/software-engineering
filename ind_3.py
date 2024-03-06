from datetime import datetime
from time import sleep


def main():
    for i in range(5):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)

if __name__ == '__main__':
    main()