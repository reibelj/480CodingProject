#HONOR CODE: This work is ours unless cited
class Node(object):

    __instance__ = None

    #Constructor
    def __init__(self,city_name=None,coordinates=None,transit_type=None):
        self.name = city_name.lower()
        self.coordinates = coordinates
        self.transit_type = transit_type.lower()
        pass

    #Two nodes are equal if they share the same name
    def __eq__(self,other):
        if (self.name == other.name):
            return True
        else:
            return False



