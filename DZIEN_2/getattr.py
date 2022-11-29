class Testowa:
    def __init__(self,abc):
        self.abc = abc

    def __getattr__(self, name):
        return f'klasa Testowa nie posiada atrybutu: {name}'

ts = Testowa("abcd")
print(ts.xyz)
print(ts.abc)
print(ts.abcd)
