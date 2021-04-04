# codewars-python

## Conway's Game of Life - Unlimited Edition

Given a 2D array and a number of generations, compute n timesteps of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

The rules of the game are:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
1. Any live cell with more than three live neighbours dies, as if by overcrowding.
1. Any live cell with two or three live neighbours lives on to the next generation.
1. Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it (i.e. [Moore Neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood)). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return ```[[]]```.)

For illustration purposes, 0 and 1 will be represented as ```░░``` and ```▓▓``` blocks respectively (PHP, C: plain black and white squares). You can take advantage of the htmlize function to get a text representation of the universe, e.g.:

```python 
print(htmlize(cells))
```

## Not very secure

In this example you have to validate if a user input string is alphanumeric. The given string is not ```nil/null/NULL/None  ```, so you don't have to check that.

The string has the following conditions to be alphanumeric:

- At least one character (```""``` is not valid)
- Allowed characters are uppercase / lowercase latin letters and digits from ```0``` to ```9```
- No whitespaces / underscore

## Write out numbers

Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.

### Examples

```
number2words(0)  ==>  "zero"
number2words(1)  ==>  "one"
number2words(9)  ==>  "nine"
number2words(10)  ==>  "ten"
number2words(17)  ==>  "seventeen"
number2words(20)  ==>  "twenty"
number2words(21)  ==>  "twenty-one"
number2words(45)  ==>  "forty-five"
number2words(80)  ==>  "eightys"
number2words(99)  ==>  "ninety-nine"
number2words(100)  ==>  "one hundred"
number2words(301)  ==>  "three hundred one"
number2words(799)  ==>  "seven hundred ninety-nine"
number2words(800)  ==>  "eight hundred"
number2words(950)  ==>  "nine hundred fifty"
number2words(1000)  ==>  "one thousand"
number2words(1002)  ==>  "one thousand two"
number2words(3051)  ==>  "three thousand fifty-one"
number2words(7200)  ==>  "seven thousand two hundred"
number2words(7219)  ==>  "seven thousand two hundred nineteen"
number2words(8330)  ==>  "eight thousand three hundred thirty"
number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"
```

## Mod4 Regex

You are to write a Regular Expression that matches any string with at least one number divisible by 4 (with no remainder). In most languages, you could do this easily by using ```number % 4 == 0```. How would you do it with Regex?

A number will start with ```[``` and end with ```]```. They may (or may not) include a plus or minus symbol at the start; this should be taken into account. Leading zeros may be present, and should be ignored (no octals here ;P). There may be other text in the string, outside of the number; this should also be ignored. Also, all numbers will be integers; any floats should be ignored.

If there are no valid numbers defined as above, there should be no match made by your regex.

So here are some examples:

```
"[+05620]" // 5620 is divisible by 4 (valid)
"[+05621]" // 5621 is not divisible by 4 (invalid)
"[-55622]" // -55622 is not divisible by 4 (invalid)
"[005623]" // 5623 invalid
"[005624]" // 5624 valid
"[-05628]" // valid
"[005632]" // valid
"[555636]" // valid
"[+05640]" // valid
"[005600]" // valid
"the beginning [0] ... [invalid] numb[3]rs ... the end" // 0 is valid
"No, [2014] isn't a multiple of 4..."  // 2014 is invalid
"...may be [+002016] will be." // 2016 is valid
```

# Who likes it?

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function ```likes :: [String] -> String```, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

```python
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
```

For 4 or more names, the number in ```and 2 others``` simply increases.

# Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.


> Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

*Courtesy of projecteuler.net*

# Square Every Digit

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

**Note**: The function accepts an integer and returns an integer

# Does my number look big in this?

A [Narcissistic Number](https://en.wikipedia.org/wiki/Narcissistic_number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcisstic:

```
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```
and 1652 (4 digits), which isn't:
```
1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
```

The Challenge:

Your code must return **true or false** depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

# Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

## Example:

```
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

# Is a number prime?

Define a function that takes one integer argument and returns logical value ```true``` or ```false``` depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Requirements

- You can assume you will be given an integer input.
- You can not assume that the integer will be only positive. You may be given negative numbers as well (or ```0```).
- **NOTE on performance**: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to ```n```, or ```n/2```, will be too slow.

# First non-repeating character

Write a function named ```first_non_repeating_letter``` that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input ```'stress'```, the function should return ```'t'```, since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input ```'sTreSS'``` should return ```'T'```.

If a string contains all repeating characters, it should return an empty string (```""```) or ```None``` -- see sample tests.

# Product of consecutive Fib numbers

The Fibonacci numbers are the numbers in the following integer sequence (Fn):


> "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ..."

such as

> "F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1."

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

> "F(n) * F(n+1) = prod."

Your function productFib takes an integer (prod) and returns an array:

```
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
```

depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying ```F(m) * F(m+1) = prod``` you will return

```
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
```

F(m) being the smallest one such as ```F(m) * F(m+1) > prod```.

## Some Examples of Return:
(depend on the language)
```
productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 
```

**Note**:
>You can see examples for your language in "Sample Tests".

