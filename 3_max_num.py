#Write your function here
def max_num(nums):
  maximum = max(nums)
  for number in nums:
    number += len(nums)
    return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
