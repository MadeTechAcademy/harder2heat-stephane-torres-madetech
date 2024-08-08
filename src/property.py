# TODO: Exploring composition, data coming in is of buildings that HAVE properties,
#  do we want a building class? should property only be a data holding class?
#  do want handlers? controllers? what do want to direct/control/manage?
#  Building has individual properties/residences that only have uprns
#  building has a list of different attributes, area, coords, osid, date etc, these are in "properties" obj within the data


# TODO currently property gets its data from a nested obj, inherits

# TODO create a building class, this has it's own id, and is made up of a property class and a attributes class
#   attribute => name, value, any point of this as it'll be essentially just a dict




class Property():
    def __init__(self, uprn):
        self.uprn = uprn

