import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_with_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("Hp")
        assert search_page.display_status_of_valid_product()

    def test_search_with_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("Dell")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_not_found_product_message().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_not_found_product_message().__eq__(
            expected_text)
