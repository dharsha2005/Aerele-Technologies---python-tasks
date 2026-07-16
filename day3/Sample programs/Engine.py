"""
Use of composition in python
"""
class Engine:
    def start(self):
        print("Engine Started")
class Start:
    def __init__(self):
        self.Engine = Engine()
    def start_Engine(self):
        return self.Engine.start()
s = Start()
s.start_Engine()