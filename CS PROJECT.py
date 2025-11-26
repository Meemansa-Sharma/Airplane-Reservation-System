import mysql.connector as s
cn=s.connect(host='localhost',user='root',passwd='12345',database='Flight_Booking_System')
print('----------------------------------------------------------------------------------------------------------------')
print('\t\t\t\t    Welcome to Airline Reservation System \t')
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('Looking for a system that deals with all types of management regarding Flights? Congratulations, you have come to the right place. ')
print('Please go through the menu options below ' ) 
print('----------------------------------------------------------------------------------------------------------------')
while (True):
    print(' 1. Add Flight  \n 2. Delete Flight  \n 3. Update Flight  \n 4. Add Passenger  \n 5. Delete Passenger  \n 6. Update Passenger  \n 7. New Booking \n 8. Delete Booking  \n 9. Update Booking \n 10. Show Flights \n 11. Show Passengers  \n 12. Show Bookings  \n 13. Searching a record \n 14. Exit The System ')
    x=int(input(' Please choose any one of the above options '))
    #To add flight record
    if (x==1):        
      cr=cn.cursor()
      i=input("Enter Flight's ID ")
      n=input("Enter Flight's Name ")
      o=input("Enter Flight's Departure ")
      d=input("Enter Flight's Arrival ")
      dd=input("Enter Departure Date ")
      dt=input('Enter Departure Time ')
      at=input('Enter Arrival Time ')
      s=input("Enter Flight's Status ")
      r=input('Enter Route ID ')
      str1="insert into flights values ({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8})".format(i,n,o,d,dd,dt,at,s,r)
     
      try :
          #To check if successfully terminated
          cr.execute(str1)
          cn.commit()
          if(cr.rowcount>0):
              print('Flight Record Added Successfully ')
    
      except:
          print('Oops! Error occurred. Try Again')

#To delete flight's record

    elif (x==2):       
        cr=cn.cursor()
        str1="select * from flights"
        try:
            cr.execute(str1)
            rec=cr.fetchall()
            if(cr.rowcount>0):
                print('----------------------------------------------------------------------------------------------------------------')
                print(' Flight ID | Flight Name | Origin | Destination | Status ')
                print('----------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{0:8} | {1:12} | {2:6} | {3:11} | {7:6}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

                    print('----------------------------------------------------------------------------------------------------------------')

        except:
            print('Oops! Error occured. Try Again')
        i=input("Enter flight's name which is to be removed ")
        str2="delete from flights where flight_name='{0}'".format(i)
        try :
          cr.execute(str2)
          cn.commit()
          if(cr.rowcount>0):
              print('Flight Record Deleted Successfully ')
        
        except:
            print('Oops! Error occurred. Try Again')

#To update flight's record
            
    elif (x==3):     
        cr=cn.cursor()
        str1="select * from flights"
        try:
            cr.execute(str1)
            rec=cr.fetchall()
            if(cr.rowcount>0):
                print('----------------------------------------------------------------------------------------------------------------')
                print(' Flight ID | Flight Name | Origin | Destination | Status ')
                print('----------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{0:8} | {1:12} | {2:6} | {3:11} | {7:6}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                    print('----------------------------------------------------------------------------------------------------------------')

        except:
            print('Oops! Error occured. Try Again')
        i=input("Enter Flight's ID which is to be updated ")
        n=input("Enter Flight's Name which is to be updated ")
        o=input("Enter Updated Flight's Departure ")
        d=input("Enter Updated Flight's Arrival ")
        dd=input("Enter Updated Departure Date ")
        dt=input('Enter Updated Departure Time ')
        at=input('Enter Upadated Arrival Time ')
        s=input("Enter Updated Flight's Status ")
        r=input('Enter Route ID ')
        str2="update flights set Origin='{2}',Destination='{3}',Departure_Date='{4}',Departure_Time='{5}',Arrival_Time='{6}',Status='{7}',Route_ID='{8}' where Flight_No={0} and Flight_Name='{1}'".format(i,n,o,d,dd,dt,at,s,r)
        
        try :
            cr.execute(str2)
            cn.commit()
            if(cr.rowcount>0):
                print('Flight Record Updated Successfully ')
        
        except:
            print('Oops! Error occurred. Try Again')

#To add passenger's record
            
    elif (x==4):    
        cr=cn.cursor()
        i=input("Enter Passenger's ID ")
        n=input("Enter Passenger's Name ")
        d=input("Enter Passenger's Date Of Birth ")
        c=input("Enter Passenger's Contact ")
        str1="insert into passengers values ({0},'{1}','{2}','{3}')".format(i,n,d,c)
        
        try :
            #To check if successfully terminated
            cr.execute(str1)
            cn.commit()
            if(cr.rowcount>0):
                print('Passenger Record Added Successfully ')
        
        except:
            print('Oops! Error occurred. Try Again')

#To delete passenger's record

    elif (x==5):
        cr=cn.cursor()
        str1="select * from passengers"
        try:
                cr.execute(str1)
                rec=cr.fetchall()
                if(cr.rowcount>0):
                    print('----------------------------------------------------------------------------------------------------------------')
                    print(' Passenger ID | Passenger Name | Date Of Birth | Contact Number ')
                    print('----------------------------------------------------------------------------------------------------------------')
                    for i in rec:
                        dob = str(i[2]) #for changing DATE datatype to STRING datatype
                        print('{0:12} | {1:16} | {2:10} | {3:14}'.format(i[0], i[1], dob, i[3]))
                        print('----------------------------------------------------------------------------------------------------------------')

        except:
                print('Oops! Error occured. Try Again')
        i=input("Enter Passenger's name whose record is to be removed  ")
        str2="delete from passengers where passenger_name='{0}'".format(i) 

        try :
            cr.execute(str2)
            cn.commit()
            if(cr.rowcount>0):
              print('Passenger Record Deleted Successfully ')
        
        except:
            print('Oops! Error occurred. Try Again')

# To update passenger's record
    
    elif (x==6): 
        cr=cn.cursor()
        str1="select * from passengers"
        try:
                cr.execute(str1)
                rec=cr.fetchall()
                if(cr.rowcount>0):
                    print('----------------------------------------------------------------------------------------------------------------')
                    print(' Passenger ID | Passenger Name | Date Of Birth | Contact Number ')
                    print('----------------------------------------------------------------------------------------------------------------')
                    for i in rec:
                        dob = str(i[2]) #for changing DATE datatype to STRING datatype
                        print('{0:12} | {1:16} | {2:10} | {3:14}'.format(i[0], i[1], dob, i[3]))
                        print('----------------------------------------------------------------------------------------------------------------')

        except:
                print('Oops! Error occured. Try Again')
        i=input("Enter Passenger's ID whose record is to be updated ")
        n=input("Enter Passenger's Name whose record is to be updated ")
        d=input("Enter Updated Passenger's Date Of Birth ")
        c=input("Enter Updated Passenger's Contact ")
        str2="update passengers set DateOfBirth='{2}', Contact_No='{3}' where Passenger_ID={0} and Passenger_Name='{1}'".format(i,n,d,c)
        
        try :
            #To check if successfully terminated
            cr.execute(str2)
            cn.commit()
            if(cr.rowcount>0):
                print('Passenger Record Updated Successfully ')
        
        except:
            print('Oops! Error occurred. Try Again')

#To add booking record
            
    elif (x==7):  
        cr=cn.cursor()
        str1="select * from flights"
        str2="select * from passengers"
        try:
            cr.execute(str1)
            rec=cr.fetchall()
            if(cr.rowcount>0):
                    print('----------------------------------------------------------------------------------------------------------------')
                    print(' Flight ID | Flight Name | Origin | Destination | Status ')
                    print('----------------------------------------------------------------------------------------------------------------')
                    for i in rec:
                        print('{0:8} | {1:12} | {2:6} | {3:11} | {7:6}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                        print('----------------------------------------------------------------------------------------------------------------')
        except:
          print('Oops! Error occurred. Try Again')
        try:
            cr.execute(str2)
            rec=cr.fetchall()
            if(cr.rowcount>0):
                        print('----------------------------------------------------------------------------------------------------------------')
                        print(' Passenger ID | Passenger Name | Date Of Birth | Contact Number ')
                        print('----------------------------------------------------------------------------------------------------------------')
                        for i in rec:
                            dob = str(i[2]) #for changing DATE datatype to STRING datatype
                            print('{0:12} | {1:16} | {2:10} | {3:14}'.format(i[0], i[1], dob, i[3]))
                            print('----------------------------------------------------------------------------------------------------------------')
        except:
          print('Oops! Error occurred. Try Again')
        i=input("Enter Flight's ID ")
        pi=input("Enter Passenger's ID ")
        c=input('Enter Class ')
        s=input('Enter Seat Number ')
        l=input('Enter Luggage ')
        se=input('Enter Status ')
        str3="insert into bookings values({0},{1},'{2}',{3},'{4}','{5}')".format(i,pi,c,s,l,se)
        try :
            cr.execute(str3)
            cn.commit()
            if(cr.rowcount>0):
              print('Booking Record Inserted Successfully ')
        
        except:
            print('Oops! Error occurred. Try Again')

#To delete booking record
            
    elif (x==8):  
        cr=cn.cursor()
        str1=" select * from bookings;" 
        cr.execute(str1)
        rec=cr.fetchall()
        if rec:
                print('--------------------------------------------------------------------------------------------------------------------------')
                print('Flight ID | Passenger ID | Class | Seat No | Luggage | Status ')
                print('--------------------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{:<9} | {:<12} | {:<15} | {:<7} | {:<7} | {:<7}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
                    print('--------------------------------------------------------------------------------------------------------------------------')


        else:
            print('Oops! Error occured. Try Again')
        i=input("Enter Passenger's id whose record is to be removed  ")
        str2="delete from bookings where passenger_id={0}".format(i)

        try :
            cr.execute(str2)
            cn.commit()
            if(cr.rowcount>0):
              print('Booking Record Deleted Sucessfully ')
        
        except:
            print('Oops! Error occured. Try Again')

 #To update booking record
            
    elif (x==9): 
        cr=cn.cursor()
        str1=" SELECT * from bookings;"
        cr.execute(str1)
        rec=cr.fetchall()
        if rec:
                print('--------------------------------------------------------------------------------------------------------------------------')
                print('Flight ID | Passenger ID | Class | Seat No | Luggage | Status ')
                print('--------------------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{:<9} | {:<12} | {:<15} | {:<7} | {:<7} | {:<7}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
                    print('--------------------------------------------------------------------------------------------------------------------------')

        else:
            print('Oops! Error occured. Try Again')
        i=input("Enter Flight's ID ")
        pi=input("Enter Passenger's ID ")
        c=input('Enter Updated Class ')
        s=input('Enter Updated Seat Number ')
        l=input('Enter Updated Luggage ')
        se=input('Enter Updated Status ')
        str2=("UPDATE bookings SET class='{2}', Seat_No={3}, Luggage='{4}', Status='{5}' " "WHERE Flight_id={0} AND passenger_id={1}" ).format(i, pi, c, s, l, se)
        try :
            cr.execute(str2)
            cn.commit()
            if(cr.rowcount>0):
              print('Booking Record Updated Sucessfully ')
        
        except:
            print('Oops! Error occured. Try Again')

#To show all flights
            
    elif (x==10):  
        cr=cn.cursor()
        str1="select * from flights"
        try:
            cr.execute(str1)
            rec=cr.fetchall()
            if(cr.rowcount>0):
                print('----------------------------------------------------------------------------------------------------------------')
                print(' Flight ID | Flight Name | Origin | Destination | Status ')
                print('----------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{0:8} | {1:12} | {2:6} | {3:11} | {7:6}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                    print('----------------------------------------------------------------------------------------------------------------')

        except:
            print('Oops! Error occured. Try Again')

#To show all passengers            
        
    elif (x==11):  
            cr=cn.cursor()
            str1="select * from passengers"
            try:
                cr.execute(str1)
                rec=cr.fetchall()
                if(cr.rowcount>0):
                    print('----------------------------------------------------------------------------------------------------------------')
                    print(' Passenger ID | Passenger Name | Date Of Birth | Contact Number ')
                    print('----------------------------------------------------------------------------------------------------------------')
                    for i in rec:
                        dob = str(i[2]) #for changing DATE datatype to STRING datatype
                        print('{0:12} | {1:16} | {2:10} | {3:14}'.format(i[0], i[1], dob, i[3]))
                        print('----------------------------------------------------------------------------------------------------------------')

            except:
                print('Oops! Error occured. Try Again')

#To show all bookings
                
    elif (x==12):  
        cr=cn.cursor()
        str2=" SELECT * from bookings;" 
        cr.execute(str2)
        rec=cr.fetchall()
        if rec:
                print('--------------------------------------------------------------------------------------------------------------------------')
                print('Flight ID | Passenger ID | Class | Seat No | Luggage | Status ')
                print('--------------------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{:<9} | {:<12} | {:<15} | {:<7} | {:<7} | {:<7}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
                    print('--------------------------------------------------------------------------------------------------------------------------')
                    
        else:
            print('Oops! Error occured. Try Again')

#To search particular booking
            
    elif(x==13):
        cr=cn.cursor()
        str1="select passenger_id from bookings"
        cr.execute(str1)
        rec=cr.fetchall()
        if(cr.rowcount>0):
                    print('----------------------------------------------------------------------------------------------------------------')
                    print(' Passenger ID of Bookings ')
                    print('----------------------------------------------------------------------------------------------------------------')
                    for i in rec:
                        
                        print('{0:12}'.format(i[0]))
                        print('----------------------------------------------------------------------------------------------------------------')
        s=input('Enter the identity number of passenger to be searched ')
        str2=" SELECT * from bookings where passenger_id={0};".format(s)
        cr.execute(str2)
        rec=cr.fetchall()
        if rec:
                print('--------------------------------------------------------------------------------------------------------------------------')
                print('Flight ID | Passenger ID | Class | Seat No | Luggage | Status ')
                print('--------------------------------------------------------------------------------------------------------------------------')
                for i in rec:
                    print('{:<9} | {:<12} | {:<15} | {:<7} | {:<7} | {:<7}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
                    print('--------------------------------------------------------------------------------------------------------------------------')
        else:
            print('Sorry, No Booking with such ID ')
            

#To exit the interface
            
    elif (x==14):  
        cn.close()
        print('\t Thank You For Using Airline Reservation System!\n \t Have A Nice Day Ahead! ')
        break

#For undesired input
    
    else:   
        print ('Please choose from the specified options only. ')
        
