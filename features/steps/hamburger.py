from behave import when, then


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.app.hamburger_menu_services.click_ham_icon()


@when('Click on Amazon Music menu item')
def click_amazon_music_icon(context):
    context.app.hamburger_menu_services.click_amazon_music_icon()


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    print("in verify_amount_of_items of hamburger.py / expected_item_count =  " + expected_item_count)
    context.app.hamburger_menu_services.verify_amount_of_items(expected_item_count)

