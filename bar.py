

class Bar():
    bars = []
    max_val = 0 if len(bars) == 0 else max(bar.val for bar in bars)

    def __init__(self, value: int):
        self.val = value
        Bar.bars.append(self)
        Bar.max_val = max(Bar.max_val, value)