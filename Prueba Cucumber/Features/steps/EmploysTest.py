from behave import *

use_step_matcher("re")


@given("I am on page choucair employs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I am on page choucair employs")


@when("I verify that the page enters correctly")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I verify that the page enters correctly")


@step("That the information posted corresponds")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("That the information posted corresponds")


@step("I press the button to go to job portal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I press the button to go to job portal")


@then("I should see an exit alert box from the employs page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I should see an exit alert box from the employs page")