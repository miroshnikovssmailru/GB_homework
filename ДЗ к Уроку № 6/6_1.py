from time import sleep


class TrafficLight:

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(15)
            print('Желтый')
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
