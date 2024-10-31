# new implementation of Decision Tree

import numpy as np
from collections import Counter

# this tree is binary decision tree, it means that the decision can be 0 or 1 => boolean decision

class DecisionNode:
    def __init__(self, left, right, decision_function, class_label=None):
        self.left: 'DecisionNode' = left
        self.right: 'DecisionNode' = right
        self.decision_function = decision_function  # funcion para decidir 
        self.class_label = class_label              # etiqueta de la clase

    def decide(self, feature):
        if self.class_label is not None: # si la etiqueta de la clase existe
            return self.class_label
        
        # evaluar la funcion de decision
        if self.decision_function(feature):
            return self.left.decide(feature)  # <--- recursion 
        else:
            return self.right.decide(feature) # <--- recursion
        
        