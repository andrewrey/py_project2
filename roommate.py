class Bill:
    """
    Object that contains data about a bill like total amount of Bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate who lives in the apartment and calculates their share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill_obj, flat_mate2):
        weight = self.days_in_house / (self.days_in_house + flat_mate2.days_in_house)
        return bill_obj.amount * weight
