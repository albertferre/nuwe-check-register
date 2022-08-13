"""This module contains the unit tests for the phone validator."""
import pytest

from src.register import Register


test_dict = {
    "task_2": (
        19.5,
        20,
        [
            ["PENNY", 1.01],
            ["NICKEL", 2.05],
            ["DIME", 3.1],
            ["QUARTER", 4.25],
            ["ONE", 90],
            ["FIVE", 55],
            ["TEN", 20],
            ["TWENTY", 60],
            ["ONE HUNDRED", 100],
        ],
        {"status": "OPEN", "change": [["QUARTER", 0.5]]},
    ),
    "task_3": (
        19.5,
        20,
        [
            ["PENNY", 0.01],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 1],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
        {"status": "INSUFFICIENT_FUNDS", "change": []},
    ),
    "task_4": (
        19.5,
        20,
        [
            ["PENNY", 0.5],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 0],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
        {
            "status": "CLOSED",
            "change": [
                ["PENNY", 0.5],
                ["NICKEL", 0],
                ["DIME", 0],
                ["QUARTER", 0],
                ["ONE", 0],
                ["FIVE", 0],
                ["TEN", 0],
                ["TWENTY", 0],
                ["ONE HUNDRED", 0],
            ],
        },
    ),
    "task_5": (
        19.5,
        2000,
        [
            ["PENNY", 0.01],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 1],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
        {"status": "INSUFFICIENT_FUNDS", "change": []},
    ),
    "task_6": (
        19.99,
        20.00,
        [
            ["PENNY", 0.01],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 0],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ],
        {"status": "CLOSED", "change": [
            ["PENNY", 0.01],
            ["NICKEL", 0],
            ["DIME", 0],
            ["QUARTER", 0],
            ["ONE", 0],
            ["FIVE", 0],
            ["TEN", 0],
            ["TWENTY", 0],
            ["ONE HUNDRED", 0],
        ]},
    ),
}


@pytest.mark.parametrize("price, cash, cid, expected", test_dict.values())
def test_register(price, cash, cid, expected):
    """This method tests the phone number validator."""
    register = Register()
    assert register.checkRegister(price, cash, cid) == expected
