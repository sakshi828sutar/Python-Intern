# Prints the grade based on the score input using if-else statements
# (A for 90-100)
#(B for 80-89)
#(c for 70-80)
# (D for 60-70)


Score = float(input('Enter your Score '))

if Score>=90 and Score<= 100:
    print("Grade A")
elif Score >= 80 and Score<= 90:
    print("Grade B")
elif Score >= 70 and Score<= 80:
    print("Grade C")
elif Score >= 60 and Score<= 70:
    print("Grade D")
else:
    print("Invalid Score. please Enter a score between 0-100 only.")

# ------------Output----------------#
# Enter your Score 71
# Grade C

