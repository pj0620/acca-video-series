from manim import *
import numpy as np

class VectorInterpolator:
    def __init__(self,points):
        self.points = points
        self.n = len(self.points)
        self.dists = [0]

        for i in range(len(self.points)):
            self.dists += [np.linalg.norm(
                self.points[i] -
                self.points[(i+1) % self.n]
            )+self.dists[i]]

    def interpolate(self,alpha):
        dist = alpha*self.dists[-1]
        idx = self.interpolate_index(dist)
        mult = (dist - self.dists[idx])/np.linalg.norm(self.points[(idx+1)%self.n]-self.points[idx])

        return self.points[idx] + \
               mult*(self.points[(idx+1)%self.n]-self.points[idx])

    def interpolate_index(self,dist):
        def is_solution(idx):
            if idx == self.n-1:
                return self.dists[idx] <= dist
            else:
                return ((self.dists[cur] <= dist) and
                        (self.dists[(cur+1)%self.n] >= dist))

        # binary search
        step_size=int(self.n / 4)
        cur=int(self.n / 2)
        while not is_solution(cur):
            if self.dists[cur] > dist:
                cur -= step_size
            else:
                cur += step_size
            step_size = max(int(step_size/2), 1)
        return cur