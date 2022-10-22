Seconds = int (input ("Enter number of seconds: ") )
Seconds = Seconds % (24 * 3600)
Hour = Seconds // 3600
Seconds %= 3600
Minutes = Seconds // 60
Seconds %= 60
Days = Seconds % 86400
print ("Days:",Days,"Hours:",Hour,"Minutes:",Minutes,"Seconds:",Seconds);