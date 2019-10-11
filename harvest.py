############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color 
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

print(make_melon_types())


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'\n{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f' - {pairing}')

print_pairing_info(make_melon_types())


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_by_code = {}

    for melon in melon_types:
        melon_type_by_code[melon.code] = melon.name

    return melon_type_by_code

print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    # Needs __init__ and is_sellable methods
    def __init__(self, code, shape, color, field, farmer):
        self.code = code
        self.shape = shape
        self.color = color 
        self.field = field 
        self.farmer = farmer 

    def is_sellable(self):
        return self.shape > 5 and self.color > 5 and self.field != 3



def make_melons(melon_types):
    """Returns a list of Melon objects."""
  
    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    melon_objects_list = [melon1, melon2, 
                          melon3, melon4, 
                          melon5, melon6, 
                          melon7, melon9]

    return melon_objects_list



print(make_melons(make_melon_types()))




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:

        if melon.is_sellable() == True:
            sellability = "(CAN BE SOLD)"
        else:
            sellability = "(NOT SELLABLE)"

        print(f'Harvested by {melon.farmer} from Field {melon.field} {sellability}')

get_sellability_report(make_melons(make_melon_types()))



