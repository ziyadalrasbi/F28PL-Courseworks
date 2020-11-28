# Arash's coursework template

# Ziyad Alrasbi, H00296507                          
# F28PL Coursework 2, Python                         <--- sanity check (think im sane)


# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.


################################################################################
# Question 1   <--- Yes, so we know what question you think you're answering


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
tocomplex and fromcomplex that map the pair (x1,y1) to the complex number x1+(y1)j and vice 
versa. You may use the python methods real and imag without comment, but not complex 
(use j directly instead).
"""
#  <--- always have the question under your nose

#####################################
# Question 1a



def cadd(c1, c2):
    # (x + yi) + (p + qi) = ((x + p), (yi + qi))
    return (c1[0] + c2[0], c1[1] + c2[1]) 


def cmult(c1,c2):
    # (x + yi)(p + qi) = (xp - yq) + (xq + yp)i
    x, y, p, q = c1[0] , c1[1], c2[0], c2[1]
    return (x*p - y*q, x*q + y*p)


#####################################
# Question 1b

def tocomplex(x1, y1):
    # adding J to the end by doing (1*J), making it complex
    return x1 + y1*1J


def fromcomplex(c):
    # converting from complex number to real
    return (c.real, c.imag)


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[~1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
"""

#####################################
# Question 2a


def seqaddi(l1, l2):
    n = len(l1) # getting length of first sequence
    result = [0] * n # making a result variable for final answer
    for i in range(n): # looping over the elements in the range of n
        result[i] = l1[i] + l2[i] # adding index 1 from first list to index 1 from 2nd list and continuing
    return result


# same process as addition except this time multiplying
def seqmulti(l1, l2):
    n = len(l1)
    result = [0] * n
    for i in range(n):
        result[i] = l1[i] * l2[i]
    return result


#####################################
# Question 2b


def seqaddr(l1, l2):
    if l1 == []:
        return []
    return [l1[0] + l2[0]] + seqaddr(l1[1:], l2[1:]) # return addition of the first indexes of the lists and then recursively go through all other element [1:]


def seqmultr(l1, l2):
    if l1 == []:
        return []
    return [l1[0] * l2[0]] + seqmultr(l1[1:], l2[1:]) # same as addition


#####################################
# Question 2c


def seqaddlc(l1,l2):
    return [l1[i] + l2[i] for i in range(len(l1))] # adding each index of both lists in the range of length of the first list


def seqmultlc(l1,l2):
    return [l1[i] * l2[i] for i in range(len(l1))] # same as addition but multiplying this time




# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3

"""
Write functions
● ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
● matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have done it the other way around that’s fine; 
just make sure to clearly explain your code). 

● matrixadd
Matrix addition, which is simply pointwise addition.
● matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may 
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.
"""


def ismatrix(m):
    if m == [[]]: 
        return True # as in OCaml if list is empty return true
    needed_length = len(m[0]) # making a variable to get the required length, starting at index 0
    for i in range(1, len(m)): # looping over elements of length m, starting at index 1
        if len(m[i]) != needed_length: # if length of the index is not the same length as index 0, return false. otherwise true
            return False
    return True


def matrixshape(m):
    if m == [[]]: # if matrix is empty just return (0, 0)
        return (0, 0)
    return (len(m), len(m[0])) # if its not empty then return the length of the original matrix and the length of first index


def matrixadd(m1,m2):
    shape = matrixshape(m1) # making a variable of type matrixshape
    result = [] # result variable to store results
    for i in range(shape[0]): # for all elements in first index 
        result.append([]) # append a list to result
        for j in range(shape[1]): # for all elements in 2nd index
            result[i].append(m1[i][j] + m2[i][j]) # do the addition calculation and then append it to the list appended earlier
    return result 


def matrixmult(m1,m2):
    shape1 = matrixshape(m1) # making 2 matrices
    shape2 = matrixshape(m2)
    result = [] # making result variable to store results
    for i in range(shape1[0]): # for all elements in first index of matrix1
        result.append([]) # append a list to result
        for j in range(shape2[1]): # second for loop to check all elements in 2nd index of matrix2
            result[i].append(0) # append another empty list with the value 0
            for k in range(shape2[0]): # this loops over until the first number is calculated
                result[i][j] += m1[i][k] * m2[k][j] # once this calculation is done, restart by adding another empty list to result and looping over again
    return result


# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
● Mutable vs immutable types. Give at least two examples of each, with explanation.
● Integer vs float types.
● Assignment = vs equality == vs identity is.
● The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).
● Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""

"""
                                        Essay on Python

    Python is a high-level object oriented programming language which, in comparison to OCaml,
    is a much more readable language because of its emphasis on the importance of code formatting
    such as indentation and capitilization. From the start, python was an easy to understand 
    language. Even once we got deeper into understanding python, it was, in general, still okay
    to understand even though it has many rules. Through the course, we learnt many new concepts
    we didn't learn in OCaml such as slicing.

                                 Mutable vs Immutable Types
    
    A mutable object by definition is an object which its values can be modified. An example of
    a type that is mutable is a list. When you define a list with a bunch of values, you are able
    to access the list and modify the contents in it without error. Here is an example of how
    this would work:
"""

def mutablelist():
    list = ['python', 'is', 'so', 'boring']
    list[3] = 'fun'
    return list

"""
    So as we can see, a list was created with a bunch of values. Then, the index 3 was accessed
    and changed so it was changed from:

                                ['python', 'is', 'so', 'boring']

    to:

                                ['python', 'is', 'so', 'fun']
    
    Another example of a mutable type is a dictionary. With a dictionary (and a set), you can't
    access the index of the items inside but you can still modify its content:
"""

def mutabledict():
    dictionary = {1: 'hello', 2: 'there'}
    dictionary[3] = 'hi'
    return dictionary

"""
    So in this example it would add change the current dictionary from:
                                {1: 'hello', 2: 'there'}
    to:
                            {1: 'hello', 2: 'there', 3: 'hi'}
    
    Immutable objects on the other hand are objects that cannot be updated. Some examples of 
    this are frozensets and tuples:
"""
e = frozenset([67, 34, 12, 45]) #frozenset
tup = (56, 78, 9, 5, 43) #tuple

"""
                                Integer vs Float Types

    In python, integers and floats are treated like in most other languages where an integer
    is a whole number and a float is a decimal number. One difference to note is that in 
    python3, dividing two integers will give an answer as a decimal if it is required whereas
    in older versions of python it would round up/down to give an integer instead. Here are
    simple examples of how integers and floats work:
"""
def checkint(): # checking int type
    a = 3
    return type(a) # will return int

def checkfloat(): # checking float type
    a = 4.764
    return type(a) # will return float

def checkround(): # checking type of number after rounding
    a = 4.764 # making a float
    return type(round(a)) # rounding it, the type will return int because it has been rounded to a whole number

def intfloatcomparison(): # checking to see if you can test the sizes between int and float
    num1 = 5 # making an int
    num2 = 3.5 # making a float
    if num1>num2: # testing to see if they can be compared, which they can, so it will return true
        return True
    else:
        return False

"""
                            Assignment, Equality and identity

    The different operators in python mean different things and it is important to get the
    notation correct or errors will be caused. A single equals sign in python is used for 
    assigning variables to values, hence the name assignment. A double equals symbol on 
    the other hand is used for checking the equality of the values that are being compared.
    "is" refers to checking if the values that are being checked have the same object 
    reference or not. Here are some examples of how they work:
"""
### Assignment ###

name = "ziyad" # a simple variable assignment
age = 19 # another example of assignment

### Equality ###

def checkequality(): 
    l1 = [] # making an empty list1
    l2 = [] # making an empty list2
    if l1 == l2: # checking the equality of the lists
        return True # will return true as they have the same values
    else:
        return False

def checkequality2(): 
    l1 = [] # making an empty list1
    l2 = ['hi'] # making another list with a different value to the first
    if l1 == l2: # checking the equality of the lists
        return True 
    else:
        return False # will return false as they do not have the same values

### Identity ###

def checkidentity(): 
    l1 = [] # making an empty list1
    l2 = [] # making another empty list2
    if l1 is l2: # checking the identity of the lists
        return True 
    else:
        return False # will return false as they do not have the same object reference

def checkidentity2(): 
    l1 = [] # making an empty list1
    l2 = l1 # making another list which has same object reference to list1
    if l1 is l2: # checking the identity of the lists
        return True # will return true as they both have the same object reference
    else:
        return False 
    
"""
                                         List Range

    The range function is another feature in python which, as in the name, does something
    in the range of another thing. For example, you can create a list within a range of 10
    which will output the numbers from 0 to 9: 
                                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]        
"""
def rangexample():
    return list(range(10))

"""
    As we can see, when this function is ran, it outputs the list within the range specified.
    Range has different ways it can be implemented. Here is an example of getting numbers 
    within a range of ten in steps of 3:
"""
def rangexample2():
    return list(range(1, 10, 3))

"""
    So when it is ran, it will return the numbers between 1 to 10 in steps of 3. Another
    thing that can be done with range is to get the numbers within a range of a number to the
    power of another number, using ** :
"""
def rangexample3():
    return len(list(range(5**5)))
"""
    Because there are too many items, returning the size of this list should return 3125,
    because 5^5 is equal to 3125. However, trying to deal with too large numbers makes 
    Python upset. An example of this would be attempting to do the same function as the one
    above, but instead of doing 5^5, you would do 5^5^5. When attempting to run that, Python
    will give you an error called an OverflowError:

                "OverflowError: Python int too large to convert to C ssize_t"

    This happens because the number is too large to deal with. Attempting to display all the
    items inside the list rather than the size could cause your PC to crash because of how
    much data would need to be outputted.



                                        Slicing
                                    
    Slicing in Python is a method of getting elements in an object from a specified index
    to another. It usually follows the notation of [start:stop] where start is the starting
    index and stop is where you want it to stop. Here is an example of slicing where there
    is a list of numbers and we want to get a specific section of it:
"""
def exampleslice():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return a[0:5]

"""
    When outputted, this will return:

                                    [1, 2, 3, 4, 5]

    Because it starts at index 0 till 5. Slicing is inclusive of the starting index (0 in 
    this case) and stops at the ending index but does excludes it (so index 5 is the number
    6 but will not get outputted). This also works with strings:
"""
def exampleslice2():
    name = "Ziyad Alrasbi"
    return name[0:5]

"""
    This will output the strings from index 0 to 5, which would just be 'Ziyad'. Slicing 
    is extremely useful in different implementations where it would be required. Notation,
    however, is extremely important when slicing. Here is an example of slicing on a list
    with the range 10^10:

                                list(range(10**10)[10:10])

    To break this down, it would first create a list with the range 10^10. Then, it would 
    slice the list down from the index 10 to 10. This basically means it would just return
    an empty list because all the elements are being sliced out of the list. The most important
    thing here is the brackets. This happens because the list is inclusive of the slicing
    when creating the list. Here is an example of a list exactly the same as the one above but
    with a small difference:

                                list(range(10**10))[10:10]

    Now to break this one down, a list is created with the range 10^10. However, the slice 
    notation excludes the end parameter so the slicing here would not do anything, therefore
    it is very important to get the parameters correct when slicing.
"""


# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5


"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
• encdat(-5) should return '-5'
• encdat(5.0) should return '5.0'
• encdat(5+5j) should return '5+5j' (not '(5+5j)'; see hint below).
• encdat('5') should return '5'


"""


def encdat(dat):
    result = str(dat) # making a result variable which is of type string, because that is what is required
    if type(dat) is complex: 
        return result[1:-1] # if the type is complex then slicing is needed so brackets aren't displayed
    else:
        return result # otherwise just return result as a string

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
• f(0) = [] (0 maps to the empty list)
• f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""


def fenc(i):
    if i == 0:
        return [] # just return empty list if i = 0
    x = fenc(i - 1) # recursively calling the function on i to make sure number is not negative
    return [x, [x]] # return x and x in brackets as per specification


def fdec(l):
    if l == []: 
        return 0 # opposite of encode. if list is empty, return 0
    current = l[0] # start at index 0
    count = 1 # start counter at 1 because we have got past if the list is empty
    while current != []: # while the list is not empty
        count +=1 # add to the counter
        current = current[0] # restart at index 0
    return count # returns the count once the list is empty


# END ANSWER TO Question 6
################################################################################


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can’t manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""


def cycleoflife():
    cycles = ['eat', 'sleep', 'code'] # making list with the cycles
    current = 0 # using this variable to check what the current cycle is
    while True:
        yield cycles[current % 3] # generator function called yield which returns a generator. current % 3 is used so that the cycle can repeat over and over
        current+=1 # making current equal to current + 1 so it can move on to the next cycle




# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""


def gendat(datum):
    if type(datum) != list: 
        return [datum] # if the datum is not a list then return the item inside a list
    result = [] # result list to store the results
    for elem in datum: # for all elements in the datum
        if type(elem) == type(5): # if the element is of type int, then append the element to the results
            result.append(elem)
        else:
            result+=gendat(elem) # otherwise recurisvely call gendat on the element
    return result



# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""





# This is not an endless generator (like you're asked to programme) this will only get primes upto the passed input or 40000
def eratosthenes(z=40000):
    # create an array of true values the size of z
    A = [True] * z
    # iterate over each value to z squared
    for x in range(2, int(z ** 0.5)):
        # if A[x] has a true value
        if A[x]:
            # iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                # set anything in the range to false
                A[z] = False
    # iterate over the array
    for y in range(2, len(A)):
        # if a value is true that index is a prime number
        if A[y]:
            # yield the current iterator location as it is a prime
            yield y




# END ANSWER TO Question 9
################################################################################
