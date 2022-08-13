"""This module contains the class Register."""

class Register():
    """Class Register"""
    values = {
        "ONE HUNDRED": 100.0,
        "TWENTY": 20.0,
        "TEN": 10.0,
        "FIVE": 5.0,
        "ONE": 1.0,
        "QUARTER": 0.25,
        "DIME": 0.1,
        "NICKEL": 0.05,
        "PENNY": 0.01,
    }

    def change(self, difference: float, cid: list) -> dict:
        """
        This method returns the change to be given to the customer.

        :param difference: the difference between the price and the cash
        :type difference: float
        :param cid: the cash in the register
        :type cid: list
        :return: a dictionary with the status and the change
        :rtype: dict
        """
        cid_dict = dict(cid)
        change = []
        for value_desc in self.values.keys():
            value_num = self.values[value_desc]

            units_needed = difference // value_num
            units_available = cid_dict[value_desc] // value_num
            units = min(units_available, units_needed)
            difference = round(difference - (units * value_num), 2)
            if units > 0:
                change.append([value_desc, units * value_num])

        if difference == 0:
            status = "OPEN"
        else:
            status = "INSUFFICIENT_FUNDS"
            change = []
        return {"status": status, "change": change}

    @staticmethod
    def get_total_value(cid) -> float:
        """
        This method returns the total value of the cash in the register given the cid.

        :param cid: the cash in the register
        :type cid: list
        :return: the total value of the cash in the register
        :rtype: float
        """
        cid_dict = dict(cid)

        return round(sum(cid_dict.values()), 2)

    def checkRegister(self, price: float, cash: float, cid: list) -> dict:
        """
        This method checks if the cash in the register is enough
        to give the customer the change and returns the status and the change.

        :param price: the price of the item
        :type price: float
        :param cash: the cash payment
        :type cash: float
        :param cid: the cash in the register
        :type cid: list
        :return: a dictionary with the status and the change
        :rtype: dict
        """
        difference = round(cash - price,2)
        available_cash = self.get_total_value(cid)
        print(available_cash, difference)
        if difference == available_cash:
            return_value = {"status": "CLOSED", "change": cid}
        else:
            return_value = self.change(difference, cid)

        return return_value
