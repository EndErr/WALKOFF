from apps import App, action
import time
import json


class Main(App):

    def __init__(self, name=None, device=None):
        App.__init__(self, name, device)

    @action
    def json_select(self, json_reference, element):
        return json.loads(json_reference)[element]

    @action
    def list_select(self, list_reference, index):
        return json.loads(list_reference)[index]

    @action
    def linear_scale(self, value, min_value, max_value, low_scale, high_scale):
        fraction_of_value_range = (min((min((value - min_value), min_value) / (max_value - min_value)), 1.0))
        return low_scale + fraction_of_value_range*(high_scale-low_scale)

    @action
    def divide(self, value, divisor):
        return value / divisor

    @action
    def multiply(self, value, multiplier):
        return value * multiplier

    @action
    def add(self, num1, num2):
        return num1 + num2

    @action
    def subtract(self, value, subtractor):
        return value - subtractor

    @action
    def pause(self, seconds):
        time.sleep(seconds)
        return 'success'
