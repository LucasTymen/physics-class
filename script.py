# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1


# Write your code below:

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
