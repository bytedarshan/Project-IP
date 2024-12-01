print("                      |----------------------------------------------------------------------|")
print("                      |                       Darshan's Billing Software                     |")
print("                      |----------------------------------------------------------------------|")
print("                      |                  Press 1 for DATA ENTRY                              |")
print("                      |                  Press 2 for BILLING                                 |")
print("                      |----------------------------------------------------------------------|")




work=input("                                         Enter here :")

print("                      |----------------------------------------------------------------------|")
if work=='1':
    print("")
    print("")
    print("")
    import entry
elif work=='2':
    print("")
    print("")
    print("")
    import bill
else:
    print("                      |                  PLEASE ENTER A VALID ENTRY                          |")
    print("                      |----------------------------------------------------------------------|")
    import home
