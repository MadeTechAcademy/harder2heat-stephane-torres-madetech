MINIMUM_EPC_RATING = "C"
MINIMUM_FAILING_AGE = 1959
COLD_CONNECTIVITY = "Standalone"
WARM_MATERIALS = ["Brick Or Block Or Stone", "Concrete"]

class Property():
    def __init__(self, uprn):
        self.uprn = uprn
        self.connectivity = ''
        self.coordinates = []
        self.OSID = ''
        self.age_last_updated = ''
        self.area_m2 = 0
