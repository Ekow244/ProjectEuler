# # 

# ## Pseudocode Stuck on Proj Euler. Sum of even valued terms in Fibonacci sequence < 4M. Pseudocode
# 1. Init variables
# 2. Set limit
# 3. Check even, var %2=0
# 5. Sum even vars
# @ace_rbk
 
# @silaslawer
#  I think it should work, what is missing?

sum_even=0

fibonacci = list(range(1,4000000))

for i in (fibonacci):
 if i % 2 == 0:
     sum_even += i

print(sum_even)