def WriteDictoFile(dic):
    outfile = input("Please Enter in the output file name: ")
    with open (outfile, "w") as f:
        for key, value in dic.items():
            f.write(f"{key} : {value}\n")

dic = {
    "A" : 1,
    "b" : 2,
    "C" : 3
}
WriteDictoFile(dic)
