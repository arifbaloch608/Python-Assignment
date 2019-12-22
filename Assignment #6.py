class car():
    def __init__(self, name, model, color, company, autoormanual):
        self.name = name
        self.model = model
        self.color = color
        self.company = company
        self.autoormanual = autoormanual
        print('Name:{} ,Model:{},Color:{},Company:{},AutoOrManual:{}'.format(self.name, self.model, self.color,
                                                                             self.company, self.autoormanual))


obj = car('cultus', 2017, 'white', 'suzuki', 'manual')

print(obj.name)
print(obj.model)
print(obj.color)
print(obj.company)
print(obj.autoormanual)