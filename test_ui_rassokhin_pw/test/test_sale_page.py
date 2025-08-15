def test_open_men_sale_page(sale):
    sale.open_page()
    sale.accept_cookie()
    sale.check_open_men_sale_page()


def test_check_tag_header(sale):
    sale.open_page()
    sale.accept_cookie()
    sale.header_page_have_tag_h1()


def test_open_women_sale_page(sale):
    sale.open_page()
    sale.accept_cookie()
    sale.check_open_women_sale_page()
