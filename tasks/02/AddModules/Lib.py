def Decor_AddModules(aModules: list):
    def Wraper(aClass):
        for Module in aModules:
            for Method in dir(Module):
                if (not Method.endswith('__')):
                    Obj = getattr(Module, Method)
                    setattr(aClass, Method, Obj)
            return aClass
    return Wraper
