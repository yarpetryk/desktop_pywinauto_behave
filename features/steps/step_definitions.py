from logging import info
from behave import given, when, then


@given('I start the App')
def step_impl(context):
    context.window_app =  context.app.top_window()
    context.window_app.wait("ready", timeout=5)
    info("Window opened successfully")

@when('I find button "{id}" and click')
def step_impl(context, id):
    el = context.window_app.child_window(best_match=id, control_type='Button').wait('enabled', timeout=5)
    el.click()

@when('I proceed to menu "{item}"')
def step_impl(context, item):
    context.window_app.menu_select(item)

@when('I select checkbox "{id}"')
def step_impl(context, id):
    checkbox = context.window_app.child_window(control_type="CheckBox", best_match=id).wrapper_object()
    status = checkbox.get_toggle_state()
    if status != 1:
        checkbox.click_input()

@when('I select "{item}" in dropdown "{id}"')
def step_impl(context, item, id):
    dropdown = context.window_app.child_window(auto_id=id, control_type="ComboBox").wrapper_object()
    dropdown.select(item)

@then('The text "{text}" should be visible')
def step_impl(context, text):
    el = context.window_app.child_window(best_match=f"Display is {text}").wait('enabled', timeout=5)
    result = el.texts()
    assert text in result[0], f'Expected "{text}", but got "{result}"'

@then('The checkbox "{id}" is selected')
def step_impl(context, id):
    checkbox = context.window_app.child_window(best_match=id, control_type="CheckBox").wrapper_object()
    status = checkbox.get_toggle_state()
    assert status == 1, f'Expected "1", but got "{status}"'

@then('The item "{item}" in dropdown "{id}" is selected')
def step_impl(context, item, id):
    dropdown = context.window_app.child_window(auto_id=id, control_type="ComboBox").wrapper_object()
    selected_item = dropdown.selected_text()
    assert selected_item == item, f'Expected "{item}", but got "{selected_item}"'
    