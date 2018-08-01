import sys;
#degrees celsius to farenheit converter
def celsius_farenheit(cel):
    f = cel * 1.8 + 32
    return(f)

def farenheit_celsius(far):
    c = (far - 32) / 1.8
    return(c)



decision = raw_input("Would you like to convert from celsius to farenheit or vice versa (enter c or f respectively): ")

if (decision == "c" or decision == "C"):
    ans = input("what is the temperature in celsius that you would like to know in farenheit: ")
    print(celsius_farenheit(ans))