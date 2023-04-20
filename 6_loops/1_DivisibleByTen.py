#Write your function here
def divisible_by_ten(nums):
  counter = 0
  for nums in counter:
    if nums % 10 == 0:
      counter +=1
      return nums

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
