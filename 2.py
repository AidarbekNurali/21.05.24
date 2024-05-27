class Number:
    def __init__(self, Maximum):
        self.Maximum = Maximum
        self.max_Maximum = max(Maximum)
        print("Max san:", self.max_Maximum)

Maximum = (3, 5, 7, 2, 9, 10)
number = Number(Maximum)