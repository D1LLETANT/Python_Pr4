class Basic:
    pass
#___________________________________________________
class AI(Basic):
    element="Air"
class GR(Basic):
    element="Ground"
class FI(Basic):
    element="Fire"
class WA(Basic):
    element="Water"
#___________________________________________________
    
class TH(AI, GR):
    pass

class SW(GR, WA):
    pass

class BF(FI, AI):
    pass

class NO(FI, WA):
    pass

class SG(SW, BF):
    pass

print(SG.element)
print(NO.element)