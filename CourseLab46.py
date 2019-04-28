name = "Zbigniew"
age = 24
daysInYear = 365
message = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message.format(name, age, age*daysInYear))
message2 = "{0:d} divided by {1:d} is  {2:d} and the rest is {3:d}"
print(message2.format(1234567890, 12345, 1234567890//12345, 1234567890 % 12345))