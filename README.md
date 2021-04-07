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

```
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

```
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

# Battle ships: Sunk damaged or not touched?

## Task
Your task in the kata is to determine how many boats are sunk damaged and untouched from a set amount of attacks. You will need to create a function that takes two arguments, the playing board and the attacks.

## Example Game
**The board**

Boats are placed either horizontally, vertically or diagonally on the board. ```0``` represents a space not occupied by a boat. Digits ```1-3``` represent boats which vary in length 1-4 spaces long. There will always be at least 1 boat up to a maximum of 3 in any one game. Boat sizes and board dimentions will vary from game to game.

**Attacks**
Attacks are calculated from the bottom left, first the X coordinate then the Y. There will be at least one attack per game, and the array will not contain duplicates.
```
[[2, 1], [1, 3], [4, 2]]
```

First attack      `[2, 1]` = `3`
Second attack `[1, 3]` = `0`
Third attack     `[4, 2]` = `1`

**Function Initialization**

```
board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]
damaged_or_sunk(board, attacks)
```

**Scoring**
1 point for every whole boat sank.
0.5 points for each boat hit at least once (**not** including boats that are sunk).
-1 point for each whole boat that was not hit at least once.

**Sunk or Damaged**
`sunk` = all boats that are sunk
`damaged` = all boats that have been hit at least once but not sunk
`notTouched/not_touched` = all boats that have not been hit at least once

**Output**
You should return a hash with the following data

```
'sunk', 'damaged', 'not_touched', 'points'
```

## Example Game Output
In our above example..

First attack: `boat 3` was damaged, which increases the `points` by `0.5`
Second attack: miss nothing happens
Third attack: `boat 1` was damaged, which increases the `points` by `0.5`
`boat 2` was untouched so `points -1` and `notTouched +1` in Javascript/Java/C# and `not_touched +1` in Python/Ruby.
No whole boats sank

**Return Hash**
```
{ 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }
```

# Your order, please

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

## Examples
```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```

# Regex Password Validation

You need to write regex that will validate a password to make sure it meets the following criteria:

- At least six characters long 
- contains a lowercase letter
- contains an uppercase letter
- contains a number

Valid passwords will only be alphanumeric characters.

# Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

# Pyramid Slide Down

## Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

```
   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
```

## Here comes the task...
Let's say that the *'slide down'* is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest *'slide down'* is ```3 + 7 + 4 + 9 = 23```

Your task is to write a function ```longestSlideDown``` (in ruby/crystal/julia: ```longest_slide_down```) that takes a pyramid representation as argument and returns its' **largest** *'slide down'*. For example,

```
longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
```

## By the way...
My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of the **Problem 18** and/or **Problem 67** on [ProjectEuler](https://projecteuler.net/).

# Only-Readable-Once list

Attention Agent.

The White House is currently developing a mobile app that it can use to issue instructions to its undercover agents.

Part of the functionality of this app is to have messages that can be read only once, and are then destroyed.

As our best undercover developer, we need you to implement a ```SecureList``` class that will deliver this functionality.

Behaviour different to the traditional list is outlined below:

- Accessing an item at any index should delete the item at that index eg:
    ``` messages=SecureList([1,2,3,4])
        print messages[1]  # prints 2
        print messages     # prints [1,3,4]
    ```
- Printing the whole list should clear the whole list eg:
    ```
    messages=SecureList([1,2,3,4])
    print messages     # prints [1,2,3,4]
    print messages     # prints []
    ```
- Viewing the representation of the list should also clear the list eg:
    ```
    messages=SecureList([1,2,3,4])
    print "my messages are: %r."%messages     # prints "my messages are: [1,2,3,4].
    print messages     # prints []
    ```
  
To complete this kata you need to be able to define a class that implements ```__getitem__()```, ```__str__()```, ```__repr__()```, and possibly ```__len__()```.

# Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

```
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
```
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# The Greatest Warrior

Create a class called `Warrior` which calculates and keeps track of their level and skills, and ranks them as the warrior they've proven to be.

## Business Rules:

- A warrior starts at level 1 and can progress all the way to 100.
- A warrior starts at rank `"Pushover"` and can progress all the way to `"Greatest"`.
- The only acceptable range of rank values is `"Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"`.
- Warriors will compete in battles. Battles will always accept an enemy level to match against your own.
- With each battle successfully finished, your warrior's experience is updated based on the enemy's level.
- The experience earned from the battle is relative to what the warrior's current level is compared to the level of the enemy.
- A warrior's experience starts from 100. Each time the warrior's experience increases by another 100, the warrior's level rises to the next level.
- A warrior's experience is cumulative, and does not reset with each rise of level. The only exception is when the warrior reaches level 100, with which the experience stops at 10000
- At every 10 levels, your warrior will reach a new rank tier. (ex. levels 1-9 falls within `"Pushover"` tier, levels 80-89 fall within `"Champion"` tier, etc.)
- A warrior cannot progress beyond level 100 and rank `"Greatest"`.

## Battle Progress Rules & Calculations:

- If an enemy level does not fall in the range of 1 to 100, the battle cannot happen and should return `"Invalid level"`.
- Completing a battle against an enemy with the same level as your warrior will be worth 10 experience points.
- Completing a battle against an enemy who is one level lower than your warrior will be worth 5 experience points.
- Completing a battle against an enemy who is two levels lower or more than your warrior will give 0 experience points.
- Completing a battle against an enemy who is one level higher or more than your warrior will accelarate your experience gaining. The greater the difference between levels, the more experinece your warrior will gain. The formula is `20 * diff * diff` where `diff` equals the difference in levels between the enemy and your warrior.
- However, if your warrior is at least one rank lower than your enemy, and at least 5 levels lower, your warrior cannot fight against an enemy that strong and must instead return "You've been defeated".
- Every successful battle will also return one of three responses: `"Easy fight", "A good fight", "An intense fight"`. Return `"Easy fight"` if your warrior is 2 or more levels higher than your enemy's level. Return `"A good fight"` if your warrior is either 1 level higher or equal to your enemy's level. Return `"An intense fight"` if your warrior's level is lower than the enemy's level.

## Logic Examples:

- If a warrior level 1 fights an enemy level 1, they will receive 10 experience points.
- If a warrior level 1 fights an enemy level 3, they will receive 80 experience points.
- If a warrior level 5 fights an enemy level 4, they will receive 5 experience points.
- If a warrior level 3 fights an enemy level 9, they will receive 720 experience points, resulting in the warrior rising up by at least 7 levels.
- If a warrior level 8 fights an enemy level 13, they will receive 0 experience points and return `"You've been defeated"`. (Remember, difference in rank & enemy level being 5 levels higher or more must be established for this.)
- If a warrior level 6 fights an enemy level 2, they will receive 0 experience points.

## Training Rules & Calculations:

- In addition to earning experience point from battles, warriors can also gain experience points from training.
- Training will accept an array of three elements (except in java where you'll get 3 separated arguments): the description, the experience points your warrior earns, and the minimum level requirement.
- If the warrior's level meets the minimum level requirement, the warrior will receive the experience points from it and store the description of the training. It should end up returning that description as well.
- If the warrior's level does not meet the minimum level requirement, the warrior doesn not receive the experience points and description and instead returns `"Not strong enough"`, without any archiving of the result.

## Code Examples:

```
bruce_lee = Warrior()
bruce_lee.level         # => 1
bruce_lee.experience    # => 100
bruce_lee.rank          # => "Pushover"
bruce_lee.achievements  # => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
bruce_lee.experience    # => 9100
bruce_lee.level         # => 91
bruce_lee.rank          # => "Master"
bruce_lee.battle(90)    # => "A good fight"
bruce_lee.experience    # => 9105
bruce_lee.achievements  # => ["Defeated Chuck Norris"]
```

# Basic DeNico

## Task
Write a function `deNico/de_nico()` that accepts two parameters:

- `key/$key` - string consists of unique letters and digits
- `message/$message` - string with encoded message

and decodes the message using the key.

First create a numeric key basing on the provided `key` by assigning each letter position in which it is located after setting the letters from `key` in an alphabetical order.

For example, for the key `crazy` we will get `23154` because of `acryz` (sorted letters from the key).
Let's decode `cseerntiofarmit` on using our `crazy` key.

```
1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n   
After using the key:
```
```
2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n
```

## Notes
- The `message` is never shorter than the `key`.
- Don't forget to remove trailing whitespace after decoding the message

## Examples
```
deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key" 
```

Check the test cases for more examples.

# Sort - one, three, two

## Hey You !
Sort these integers for me ...

By name ...

Do it now !

## Input
Range is `0-999`

There may be duplicates

The array may be empty

## Example
- Input: 1, 2, 3, 4
- Equivalent names: "one", "two", "three", "four"
- Sorted by name: "four", "one", "three", "two"
- Output: 4, 1, 3, 2

## Notes
- Don't pack words together:
- e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
- e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
- Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
- e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
- e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"

# Roman Numerals Helper

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

## Examples
```
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
```