HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """


    st = abs(street(a) - street(b))
    ave = abs(avenue(b) - avenue(a))
    return st + ave


    """intersection_one = street(inter)
    intersection_two = avenue(inter)

    distance = abs(intersection_one) - abs(intersection_two)
        retun distance 



    a = abs(intersection_one[0] - intersection_two[0]
    b = abs(interection_one[1]) - interection_two[1]

        return a + b"""


"""intersection_one = intersection_1(a) - intersection_2(b)
    intersection_two = intersection_2(a) - intersection_1(b)
        return abs ( intersection_one - intersection_two)"""



def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """

    s = [round((x)**(1/2)) for x in s if round((x)**(1/2))**2 == x]
    return s


    """so if square rooting x results in a perfect square , rounding
    it doesn't do anthing so it will just return what we want, a perfect
    square. the way you check that is that when you round it
    if squaring that number == x, then it was a perfect square. 

    (sqrt(x))^2 returns x <-- these are perfect squares"""



def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    
    if n <= 3:
        return n
    return g(n-1) + 2 * g(n-2) + 3 * g(n-3)



def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """

    if n <= 3:
        return n
    else:
        x, y, z = 3, 2, 1
        while n > 3:
            x, y, z = x + 2*y + 3*z, x, y
            n = n-1
        return x


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    

    def helper (k, increment, value):
        if k == n:
            return value
        if k%7==0 or has_seven(k):
            return helper(k+1, increment*(-1), value+increment*(-1))
        return helper(k+1, increment*1, value + increment*1)

    return helper(1,1,1)


    """"going down sequence. If condition is met, change
    direction. No? Keep going. Once you hit last N, return that nth 
    element(the index I believe")"""


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """

    def count(coins, amount):
        if coins == amount:
            return 1
        elif coins < 0:
            return 0
        elif coins > amount:
            return 0
        else:
            minimum_partition = count(coins, amount-coins)
            not_minimum_partition = count(2*coins, amount)
            return minimum_partition + not_minimum_partition

    return count(1,amount)



    """powers of two in terms of largest power
    of 2 until get to n""" 


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
