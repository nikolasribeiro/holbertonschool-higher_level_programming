#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ 
    Think this exercise like a Venn Diagram.
    | = Union
    & = Intersection
    - = Diferent
    ^ = Symmetric difference
    
    """
    return (set_1 ^ set_2)