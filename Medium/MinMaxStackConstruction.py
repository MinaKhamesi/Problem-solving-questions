class MinMaxStack:
	def __init__(self):
		self.stack = []
    def peek(self):
		if len(self.stack) == 0:
			return
        return self.stack[-1]['num']

    def pop(self):
		if len(self.stack) == 0:
			return
        num = self.stack[-1]['num']
		self.stack.pop()
		return num

    def push(self, number):
        if len(self.stack) == 0:
			self.stack.append({'num':number, 'min': number, 'max':number})
		else:
			minToThisPoint = min(number,self.stack[-1]['min'])
			maxToThisPoint = max(number, self.stack[-1]['max'])
			self.stack.append({'num':number, 'min': minToThisPoint, 'max': maxToThisPoint})

    def getMin(self):
		if len(self.stack) == 0:
			return
        return self.stack[-1]['min']

    def getMax(self):
		if len(self.stack) == 0:
			return
        return self.stack[-1]['max']
