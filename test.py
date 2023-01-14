
def test (org):
    test = ""
    for i in range (0,len(org)):
        test += org[len(org)-1-i]
    return test == org


print(test("bob"))
