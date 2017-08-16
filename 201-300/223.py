class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E < A:
            A,B,C,D,E,F,G,H = E,F,G,H,A,B,C,D
        one = (E <= C and B <= H <= D)
        two = (E <= C and B <= F <= D)
        three = (E <= C and H > D and F < B)
        if one and two:
            diff = (G-E)*(H-F) if G <= C else (C-E)*(H-F)
        elif one:
            diff = (G-E)*(H-B) if G <= C else (C-E)*(H-B)
        elif two:
            diff = (G-E)*(D-F) if G <= C else (C-E)*(D-F)
        elif three:
            diff = (G-E)*(D-B) if G <= C else (C-E)*(D-B)
        else:
            diff = 0
        return (C-A)*(D-B) + (G-E)*(H-F) - diff
