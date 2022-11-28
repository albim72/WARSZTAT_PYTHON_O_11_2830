def zewnetrzna():
    x = "lokalnie"
    def wewnetrzna():
        nonlocal x
        x = "nielokalnie"
        print(f"wewnętrzne x: {x}")
    wewnetrzna()
    print(f"zewnętrzne x: {x}")
