class Vault:

    def __init__(self, galleons=0, sick=0, knut=0):
        self.galleons = galleons
        self.sick = sick
        self.knut = knut

    def __str__(self):
        return f'{self.galleons} Galleons, {self.sick} Sick, {self.knut} Knut'

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sick = self.sick + other.sick
        knut = self.knut + other.knut
        return Valut(galleons, sick, knut)

potter = Vault(100, 20, 10)
print(potter)