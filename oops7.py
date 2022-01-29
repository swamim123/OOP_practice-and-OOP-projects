class Electronics_devices():
    devices=4

    def __init__(self,amobile,atv,aradio,awatch):
        self.mobile=amobile
        self.tv=atv
        self.radio=aradio
        self.watch=awatch

    def elect_gagets(self):
        return f"this is {self.mobile} and this is {self.tv} and this {self.radio} and last {self.watch}"

class Pocket_gaget(Electronics_devices):
    pocketdevices= 3

    def __init__(self,ipod,emobile,ewatch):
        self.ipod=ipod
        self.emobile=emobile
        self.ewath=ewatch

    def epocket_gaget(self):
        return f"These are pocket gaget{self.ipod} and {self.ewath} and {self.emobile}"

class Phone(Pocket_gaget):
    phones= 2

    def  __init__(self,nokia,samsung):
        self.nokia=nokia
        self.samsung=samsung

    def phone_c(self):
        return f"These are new company {self.nokia} and {self.samsung}"

Dad = Electronics_devices("Nokia","Sony","CRadio","Sonota")
Son = Pocket_gaget("eIpod","Redme","Rolex")
Grandson = Phone("700","14000")

print(Dad.elect_gagets())
print(Son.epocket_gaget())
print(Grandson.phone_c())