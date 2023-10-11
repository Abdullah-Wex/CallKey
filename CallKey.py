class CallKey:
    from typing import Literal
    def __init__(self, value, key: str | None = None) -> None:
        self.value = value
        self.type = type(value)
        self.key = key

        def inValue(key: str,unique=False, find = False) -> CallKey:
            try:
                if find:
                    key = list(filter(lambda x: x.endswith(key),self.value.keys()))[0]
                if unique:
                    return CallKey(self.value[key][0], key)
                else:
                    return CallKey(self.value[key], key)
            except:
                return CallKey('', key)
        self.inValue = inValue

    def resign(self,value):
        self.value = value

    def eachInValue(self, key: str):
        result = []
        for i in self.value:
            result.append(CallKey(i[key], key))
        return CallKey(result, self.key+'_'+key)

    def allInValue(self, keys: Literal):
        allResult = []
        for v in self.value:
            x = CallKey(v)
            result = []
            for k in keys:
                result.append(x.inValue(k))
            allResult.append(result)
        return CallKey(allResult)

    def revers_Bool(self):
        if self.value == '' or self.value == None:
            return False
        else:
            if self.type == bool:
                return self.value
            else:
                return True

    def filter(self,function,unique=False):
        if type(self.value) != list and type(self.value) != dict:
            return
        result = CallKey(self.value,self.key)
        if type(self.value) == dict:
            result.value = dict(filter(function,result.value))
        else:
            result.value = list(filter(function,result.value))
        if unique:
            result.value = result.value[0]
        return result

    def map(self,function,unique=False):
        if type(self.value) != list and type(self.value) != dict:
            return
        result = CallKey(self.value,self.key)
        if type(self.value) == dict:
            result.value = function(result.value)
        else:
            result.value = list(map(function,result.value))
            if unique:
                result.value = result.value[0]

        return result

    def function(self,function):
        # if type(self.value) != list and type(self.value) != dict:
        #     return
        result = CallKey(self.value,self.key)
        result.value = function(result.value)
        return result

    def find(self, function, findAll=False,returnIndex=True):
        if self.type is list:
            result = []
            for index in range(len(self.value)):
                condition = function(self.value[index])
                if type(condition) is bool and condition:
                    result.append(index)
            if findAll:
                if returnIndex:
                    return result if len(result)>0 else None
                else:
                    return [self.value[i] for i in result] if len(result)>0 else None
            else:
                if returnIndex:
                    return None if len(result)==0 else result[0]
                else:
                    return None if len(result)==0 else self.value[result[0]]
        else:
            raise Exception('this function worked only with list type')
    
    def pop(self, function,returnValues = False):
        if self.type is list:
            indexs = self.find(function,True)
            if indexs is not None:
                indexs = sorted(indexs,reverse=True)
                if returnValues:
                    return [self.value.pop(i) for i in indexs]
                else:
                    [self.value.pop(i) for i in indexs]
            else:
                print('Nothing found')
        else:
            raise Exception('This function worked only with list type')

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        if type(self.value) == CallKey:
            return str(self.value)
        else:
            return str(self.value)

    def __str__(self) -> str:
        return str(self.value)
