"""
These tests are not complete yet - I will be writing them in the next couple of days. I'll push the changes to GitLab as soon
as I write all the tests.

"""
import py_cw
import unittest
from random import randint

class UnitTests(unittest.TestCase):

	def test_q1a(self):
		s = py_cw.cadd((1, 0), (0, 1))
		p = py_cw.cmult((3, 2), (9, 6))
		assert s == (1, 1) and p == (15, 36)


	def test_q1b(self):
		assert py_cw.tocomplex(1, 2) == (1 + 2j) and py_cw.fromcomplex(1 + 1j) == (1, 1)


	def test_q2a(self):
		assert py_cw.seqaddi([1, 2, 3, 4], [2, 3, 4, 5]) == [3, 5, 7, 9] and py_cw.seqmulti([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 6, 12, 20]


	def test_q2b(self):
		assert py_cw.seqaddr([1, 2, 3, 4], [5, 4, 3, 2]) == [6, 6, 6, 6] and py_cw.seqmultr([1, 2, 3, 4], [5, 4, 3, 2]) == [5, 8, 9, 8]


	def test_q2c(self):
		assert py_cw.seqaddlc([1, 2, 3, 4], [5, 4, 3, 2]) == [6, 6, 6, 6] and py_cw.seqmultlc([1, 2, 3, 4], [5, 4, 3, 2]) == [5, 8, 9, 8]


	def test_q3_ismatrix(self):
		assert (not py_cw.ismatrix([[2,3,4], [3,2,6,7], [2,3,4]])) and py_cw.ismatrix([[1,2,3], [3,4,6]])


	def test_q3_matrixshape(self):
		m = [[1,2,3], [3,4,6]]
		assert py_cw.matrixshape(m) == (2, 3)


	def test_q3_matrixadd(self):
		m1 = [[1,2,3], [3,4,6]]
		m2 = [[5,6,7], [7,6,4]]
		assert py_cw.matrixadd(m1, m2) == [[6, 8, 10], [10,10,10]]


	def test_q3_matrixmult(self):
		m1 = [[2,3,4], [7,8,9]]
		m2 = [[1,0], [3,6], [8,2]]
		assert py_cw.matrixmult(m1, m2) == [[43,26], [103,66]]


		################ ESSAY TESTS #####################

	def test_q4_mutablelist(self):
		assert py_cw.mutablelist() == ['python', 'is', 'so', 'fun']

	def test_q4_mutabledict(self):
		assert py_cw.mutabledict() == {1: 'hello', 2: 'there', 3: 'hi'} 

	def test_q4_checkint(self):
		assert py_cw.checkint() == int 
	
	def test_q4_checkfloat(self):
		assert py_cw.checkfloat() == float    

	def test_q4_checkround(self):
		assert py_cw.checkround() == int     

	def test_q4_intfloatcomparison(self):
		assert py_cw.intfloatcomparison() == True

	def test_q4_checkequality(self):
		assert py_cw.checkequality() == True

	def test_q4_checkequality2(self):
		assert py_cw.checkequality2() == False

	def test_q4_checkidentity(self):
		assert py_cw.checkidentity() == False

	def test_q4_checkidentity2(self):
		assert py_cw.checkidentity2() == True  
	
	def test_q4_rangexample(self):
		assert py_cw.rangexample() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	
	def test_q4_rangexample2(self):
		assert py_cw.rangexample2() == [1, 4, 7]
	
	def test_q4_rangexample3(self): 
		assert py_cw.rangexample3() == 3125       

	def test_q4_exampleslice(self): 
		assert py_cw.exampleslice() == [1, 2, 3, 4, 5]

		############## END ESSAY TESTS ###################
	def test_q5(self):
		assert py_cw.encdat(-10)=='-10' and py_cw.encdat(10.4) == '10.4' and py_cw.encdat(5+4.5j)=='5+4.5j' and py_cw.encdat(345)=='345'


	def test_q6_fenc(self):
		assert py_cw.fenc(4)==[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]


	def test_q6_fdec(self):
		assert py_cw.fdec([[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]])==4


	def test_q7(self):
		n = randint(100, 1000)
		li = ['eat', 'sleep', 'code']
		g = py_cw.cycleoflife()
		y = None
		for _ in range(n):
			y = next(g)
		assert y == li[(n % 3) - 1]


	def test_q8(self):
		assert py_cw.gendat([5,5,[5,[]],[],[5],[[5]]]) == [5,5,5,5,5]


	def test_q9(self):
		p = None
		e = py_cw.eratosthenes()
		for _ in range(22):
			p = next(e)
		assert p == 79

if __name__ == "__main__":
	unittest.main()




