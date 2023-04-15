# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

#step 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#step 2
f100_in_celsius = f_to_c(0)
print(f100_in_celsius)

#step 3
def c_to_f(c_temp):
  f_temp = c_temp *(9/5) + 32
  return f_temp

#step 4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Step 5
def get_force(mass, acceleration):
  return mass * acceleration

#step 6
train_force = get_force(train_mass, train_acceleration)
print(train_force)
#step 7
#step 8
#step 9
#step 11
#step 12
#step 13
