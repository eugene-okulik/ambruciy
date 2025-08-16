def test_all_el(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.accept_cookie()
    eco_friendly.check_number_of_products_on_a_page()


def test_open_card_product(eco_friendly, product_card):
    eco_friendly.open_page()
    eco_friendly.accept_cookie()
    name_product = eco_friendly.open_card_product()
    product_card.check_product_card(name_product=name_product)


def test_sorted_by_price(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.accept_cookie()
    eco_friendly.check_sort_by_price()
