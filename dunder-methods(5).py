class person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __contains__(self, item):
        if item in self.name:
            return True


p1 = person("Sam", "Canada")
p2 = person("max", "angola")

print(p1.name)

print("Sam" in p1)
