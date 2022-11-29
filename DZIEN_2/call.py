class Specjalna:
    def __init__(self):
        print("instancja została utworzona")

    def __call__(self):
        print("instancja wołana po specjalnej metodzie...")

ob = Specjalna()
ob()
