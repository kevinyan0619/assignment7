'''
Created on Nov 14, 2016

@author: sj238
'''
import re
from UserError import *

class interval(object):
    def __init__(self, input_interval):
        input_interval = input_interval.strip()
        if input_interval == '':
            raise ValueError('No empty string')
        if type(input_interval) is not str:
            raise TypeError('Interval must be a string.')
        self.lower_bound = input_interval[0]
        if self.lower_bound == '(':
            exclusive_lower = True
        elif self.lower_bound == '[':
            exclusive_lower = False
        else:
            raise ValueError("Invalid lower bound")
        self.upper_bound = input_interval[-1]
        if self.upper_bound == '(':
            exclusive_upper = True
        elif self.upper_bound == '[':
            exclusive_upper = False
        else:
            raise ValueError("Invalid upper bound")
        comma = input_interval.index(',')
        self.lower_value = int(input_interval[1:comma])
        self.upper_value = int(input_interval[comma+1:-1])
        if self.lower_value > self.upper_value:
            raise ValueError("Lower value cannot be bigger than upper value")
        self.lower_value + 1 if exclusive_lower else self.lower_value
        self.upper_value - 1 if exclusive_upper else self.upper_value
        self.left = input_interval[:comma]
        self.right = input_interval[comma+1:]
    def __repr__(self):
        return self.left + ',' + self.right
    
    def __or__(self, interval):
        return mergeIntervals(self, interval)

    def __eq__(self, interval):
        return (self.lower_value == interval.lower_value) and (self.upper_value == interval.upper_value)

    def __ne__(self, interval):
        return (self.lower_value != interval.lower_value) or (self.upper_value != interval.upper_value)


def Rearrange(interval1, interval2):
    if interval1.lower_value > interval2.lower_value:
        left_interval = interval1
        right_interval = interval2
    else:
        left_interval = interval2
        right_interval = interval1
    return left_interval, right_interval

def mergeIntervals(interval1, interval2):
    left_interval, right_interval =  Rearrange(interval1, interval2)
    if left_interval.upper_value < right_interval.lower_value - 1:
        raise ValueError('Intervals should be ovelap or adjacent')
    else:
        if left_interval.lower_valuie == right_interval.lower_value and right_interval.lower_bound > left_interval.lower_bound:  
            merge_left = right_interval.left 
        else:
            merge_left = left_interval.left
        if left_interval.upper_value > right_interval.upper_value:
            merge_right = left_interval.right
        elif left_interval.upper_value == right_interval.upper_value and left_interval.upper_bound > right_interval.upper_bound:
            merge_right = left_interval.right
        else:
            merge_right = right_interval.right
        return merge_left + ',' + merge_right

def mergeOverlapping(intervals):
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals, key=lambda x: interval(x).lower_value)
    merged = []
    for i in range(1, len(intervals)):
        try:
            new = mergeIntervals(interval(merged[-1]),interval(intervals[i]))
            merged[-1] = new
        except ValueError('Intervals should be ovelap or adjacent'):
            merged.append(intervals[i])
    return merged
        
        
def insert(intervals, newint):
    return mergeOverlapping(intervals + [newint])
     
        
            
        
        
        