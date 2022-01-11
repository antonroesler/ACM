from math import gcd

class Solution:
	def hasGroupsSizeX(self, deck: List[int]) -> bool:
		d = {}
		for i in deck:
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		arr = []
		for x in deck:
			if d[x] == 1:
				return False
			arr.append(P_F(d[x]))
		s = set(arr[0])
		for z in arr:
			i_s = []
			for i in s:
				if i not in z:
					i_s.append(i)
			for i in i_s:
				s.remove(i)
		if len(s) > 0:
			return True
		else:
			return False