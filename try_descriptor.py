





class Value:


    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self
        #print('comm', obj.commission)
        return self.amount * (1 - obj.commission)

    def __set__(self, obj, amount):
        if obj is None:
            return self
        #print('set ', amount)
        self.amount = amount
