# # Python Function Challenges
# 1. Write a function named `sum_to()` that takes a number parameter `n` and returns the sum of the numbers from 1 to n. For example:
# ```python
# sum_to(6)  # returns 21
# sum_to(10) # returns 55
# ```

def sum_to(n):
  nums=[n]
  for i in range(n):
    nums.append(i)
  return sum(nums)
print('sum_to: ',sum_to(6))

# 2. Write a function named `largest()` that takes a list parameter and returns the largest element in that list. You can assume the list contents are all *positive* numbers. For example:
# ```python
# largest([10, 4, 2, 231, 91, 54])  # returns 231
# largest([1,2,3,4,0])  # returns 4
# ```

def largest(my_list):
  return max(my_list)
print('largest: ',largest([10, 4, 2, 231, 91, 54]))

# 3. Write a function named `occurances()` that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
# ```python
# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0
# ```

def occurences(whole_string, partial_string):
  return whole_string.count(partial_string)
print('occurences: ',occurences('fleep floop', 'e'))

# 4. Write a function named `product()` that takes an *arbitrary* number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on `*args`).

def product(*stuff):
  prod = 1
  for item in stuff:
    prod *= item
  return prod
print('product: ',product(2,2,10))

# # Python vs. Javascript - The Differences
# ### Get Name 
# Write a method that accepts a name from the user and then returns it. Here's the javascript: 
# ```
# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };
# ```
def get_name():
  name=input('What is your name?: ')
  return print('get_name: ',name)
get_name()

# ### Reverse It 
# Write a method that reverses a string. Here's the javascript:
# ```
# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";
#   let reverse = "";
#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };
#   consloe.log(reverse);
# };
# ```

def reverse(my_word):
  return my_word[::-1]
print('reverse: ',reverse('hello'))

# ### Swap Em 
# Write a method that swaps the values of two variables around. Here's the javascript:
# ```
# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;
#   temp = b;
#   b = a;
#   a = temp;
#   console.log("a is now " + a + ", and b is now " + b);
# };
# ```
def swap_em(first,second):
  holding=[first,second]
  first=holding[1]
  second=holding[0]
  return(first,second)
print('swap_em: ',swap_em(1,2))

# ### Multiply Array 
# Write a method that multiplies all numbers in a given array and returns the final product. Here's the javascript:
# ```
# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };
#   let total = 1;
#   // let total = ary[0];
#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };
#   return total;
# };
# ```
def multiply_array(numbers):
  prod=1
  for number in numbers:
    prod *= number
  return prod
print('multiply_array: ',multiply_array([1,2,10]))

# ### Fizz Buzzer 
# Write a method that takes a number argument and returns "fizz" if the number is divisible by three, "buzz" if the number is divisible by five, and "fizzbuzz" if it's divisible by both. Here's the javascript:
# ```
# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }
# ```
def fizz_buzz(number):
  word=''
  if number %3 == 0 and number %5 ==0:
    word='fizzbuzz'
  elif number %3 == 0:
    word = 'fizz'
  elif number %5 ==0:
    word = 'buzz'
  else:
    word= 'archer'
  return(word)
print('fizz_buzz: ',fizz_buzz(17))

# ### Nth Fibonacci 
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:
# ```
# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");
#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }
#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };
# ```
def nth_fib_number(index):
  fibs=[1,1]
  for i in range(index-2):
    first=fibs[i]
    second=fibs[i+1]
    new_fib=first+second
    fibs.append(new_fib)
  return fibs[index-1]
print('nth_fib_number: ',nth_fib_number(6))

# ### Search Array 
# Write a method that searches through an array for a value and returns true or false depending on whether or not the value is present in the array. Here is the javascript:
# ```
# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };
# ```
def search_array(feild, value):
  if value in feild:
    return True
  else:
    return False
print('search_array: ',search_array([1,2,3,4,5],5))

# ### Palindrome 
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:
# ```
# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };
# ```

def is_palindrome(word):
  if word[::-1] == word:
    return True
  else: 
    return False
print('is_palindrome: ',is_palindrome('aha'))

# ### hasDupes
# Write a method that checks whether or not an array has any duplicates. Here is the javascript:
# ```
# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };
# ```
def has_dupes(array):
  true_or_false=''
  for item in array:
    if array.count(item)>0:
      true_or_false= True
    else:
      true_or_false= False
  return(true_or_false)
print('has_dupes: ',has_dupes([1,2,0]))