
name=input("enter the name:")
contactno=input("enter contact num:")
email=input("enter the email id:")
cityy=input("enter the city:")
b=True
while b:
    print("                                                             Trazon self driving car                         \n\n\n\n")
    import time
    datee=time.strftime("%x")
    timee=time.strftime("%X")
    day=time.strftime("%A")
    print("Date--- %s                                                                                                                    Time-- %s"%(datee,timee))
    (c,cc,ccc,cccc)=(True,True,True,True)
    citynames=[[1,"banglore"],[2,"chennai"],[3,"mumbai"],[4,"kolkata"],[5,"delhi"]]
    car=[[1,"mini ",30,10,["I10","I20","Alto"]],[2,"micro",40,20,["Shift","Hundai","suzuki"]],[3,"prime",50,30,["Duster","Bolero","xylo"]],[4,"lux  ",90,50,["Benz","Audi","Bmw"]]]
    date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    month=[1,2,3,4,5,6,7,8,9,10,11,12]
    time=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    print("      City names")
    for i in citynames:
        print("  %s %s"%(i[0],i[1]))
    while c:    
        city=input("enter city No: ")
        if city in["1","2","3","4","5"]:
            c=False
            city=int(city)
            city=city-1
            print("you are choosing %s"%citynames[city][1])
        else:
            print("choose city num in correct way")
    print(" AvailableCars Perhour charge  Extra onehour charge ")
    for i in car:
        print("%s %s       %s               %s"%(i[0],i[1],i[2],i[3]))
    while cc:
        carr=input("choose your carr: ")
        if carr in["1","2","3","4"]:
            cc=False
            carr=int(carr)
            carr=carr-1
            print("Thankyou for choosing %s"%car[carr][1])
        else:
            print("choose city num in correct way")
    print("1 %s \n2 %s \n3 %s"%(car[carr][4][0],car[carr][4][1],car[carr][4][2]))
    while ccc:
        carmodel=input("Enter your car: ")
        if carmodel in["1","2","3"]:
            ccc=False
            carmodel=int(carmodel)
            print("Your journey start with %s "%car[carr][4][carmodel-1])
        else:
            print("choose city num in correct way")
    while cccc:        
        pickupmonth=int(input("Enter Month to pickup"))
        if pickupmonth in month:
            startdate=int(input("Enter the Date"))
            pickuptime=int(input("Enter pickup time"))
            droptime=int(input("Enter Drop time"))
            if (pickuptime and droptime in time)and(startdate in date):
                cccc=False
                traveltime=droptime-pickuptime
                if traveltime in time:
                    print("pickup at %s:%s:2018\n"%(startdate,pickupmonth))
                    print("pickuptime is:%s:00\n"%pickuptime)                                                                                                         
                    print("droptime is:%s:00\n"%droptime)
                    charge=traveltime*(car[carr][2])
                    extracharge=traveltime*(car[carr][3])
                    print("traveltime is:0%s:00\n"%traveltime)
                else:
                    print("Please enter valid pickup and droptime\n ")
                    cccc=True
            else:
                print("you enter wrng date or time pls re enter")
        else:
            print("Please Reenter Month Date Time ")
    b=False                    
print(" .....................\ntravelr name:%s\ncontact no:%s\nemail id:%s\nboarding city:%s\n.......................\n "%(name,contactno,email,cityy))
print("\ncharge:%s"%charge)
print("\nextra charge:%s\n"%extracharge)
print("GST         =%s .Rs (18%%)"%(charge+extracharge/100*18))
print("VAT         =%s  .Rs (4%%)"%(charge+extracharge/100*4))
print("CGST        =%s  .Rs (4%%)"%(charge+extracharge/100*4))
print("Actual price=%s .Rs "%(charge+extracharge))
print(" ---------------------------------------")
print("total       =%s .Rs"%((charge+extracharge/100*18)+(charge+extracharge/100*18)+(charge+extracharge/100*18)+(charge+extracharge)))
print(" ")
print("      ..........................................................Thankyou for booking...........................       " )



     
        
   

        

    
                                                                                                         


 
      

