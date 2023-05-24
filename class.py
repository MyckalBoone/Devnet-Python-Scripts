Router:

    def __init__(self, model, version, ip_add):
        self.model = model
        self.version = version
        self.ip_add = ip_add

    def getdesc(self):
        desc = f'Router Model			:{self.model}\n'\
               f'Software version		:{self.version}\n'\
	       f'Router Management Address	:{self.ip_add}'
        return desc

rtr1 = Router('iosv', '12.46.4', '10.10.10.10')
rtr2 = Router('ios4221', '13.3.1', '10.10.10.11')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), sep='')

