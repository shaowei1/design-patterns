class ProtectMe:
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "kivi"

    @property
    def name(self):
        return self.__name

    def __python(self):
        print("I love Python.")


if __name__ == "__main__":
    p = ProtectMe()
    # print(p.__name)  AttributeError: 'ProtectMe' object has no attribute '__name'
    # print(p.__python())
    print(p.name)
