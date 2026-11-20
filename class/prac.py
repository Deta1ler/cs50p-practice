class StepCounter:
    def __init__(self, steps=0):
        if steps < 0:
            raise ValueError("Хуйня")
        self.steps = steps

    def add_steps(self, count):
        if count <= 0:
            raise ValueError("Хуйня2")
        self.steps = self.steps + count

    def reset(self):
        self.steps = 0


counter = StepCounter(100)
counter.add_steps(-2)
print(counter.steps)


        