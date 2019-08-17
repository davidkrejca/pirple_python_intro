# Checker fuction _homework3 _If statements

def check(Snow, Sunny, Temperature):
    Snow = "Bad"
    Sunny = "False"
    Temperature = "10"

    if Snow == "Good" and Sunny == True or Temperature == "-10":
        return "True"
    elif Snow == "Good" or Sunny == True and Temperature == "-10":
        return "True"
    else:
        print ('False')