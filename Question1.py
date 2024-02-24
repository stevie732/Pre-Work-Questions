
# Question 1. 
def hello_name(user_name):
    print("In hello_name", user_name)
greeting = input("Enter Name: ")
print("Hello", greeting)

# Question 1-cont. Asks about work
def computepay(hours, rate):
    print("In computepay", hours, rate)

kk = input("Do You Have A Job?: ")
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.6)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:",xp)
