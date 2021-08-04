from behave import *

use_step_matcher("re")


@given("I am on page Choucair Home")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I am on page Choucair Home")


@when("I press the employs button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I press the employs button")


@then("I should be on the page of employs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("I should be on the page of employs")