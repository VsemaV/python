from time import sleep
from itertools import cycle


class TrafficLights:

    def __init__(self):
        self.__color = (('Красный', 7), ('Желтый', 2), ('Зеленый', 10))

    def running(self):
        for color, sec in cycle(self.__color):
            if color == 'Красный':
                print('({} - Стоп)'.format(color))
            elif color == 'Желтый':
                print('({} - Приготовиться)'.format(color))
            else:
                print('({} - Стартуем)'.format(color))
            sleep(sec)


traffic_light = TrafficLights()
traffic_light.running()
