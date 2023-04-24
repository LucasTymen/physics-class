#Write your function here
def over_nine_thousand(lst):
  new_sum = 0
  for number in lst:
    number += new_sum
    return new_sum
  print(new_sum)
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
