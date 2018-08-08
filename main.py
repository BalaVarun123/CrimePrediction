form pred import *
print("Crime predictor:")
option = None
while(True):
    print("""Your options are :
    C - Create a new network
    T - Train a network
    L - list all networks
    P - predict
    E - exit
    """)
    option = input("Enter your choice:")
    if option == 'C':
        createNetwork()
    elif option == 'T'
        cityname = input("Enter city name:")
        if cityname not in cities : 
            print("City name : %s doesn't exits"%cityname)
            continue
        filename = input("Enter filename:")
        learn(cityname,filename)
    elif option == 'L':
        print("A network exists for these cities:")
        for city in cities:
            print(city)
    elif option == 'P':
        cityname = input("Enter city name:")
        if cityname not in cities:
            print("City name : %sdoesn't exits"%cityname)
            continue
            city = cities[cityname]
        print("Enter Time:")
        city.ilayer[0]  int(input("MM:"))
        city.ilayer[1] = int(input("HH:"))
        print("Enter Date:")
        city.ilayer[2] = int(input("DD:"))
        city.ilayer[3] = int(input("MM:"))
        city.ilayer[4] = int(input("YY:"))
        city.predict()
    elif option == 'E':
        exit()



