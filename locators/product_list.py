""""Элементы на странице каталога"""

from selenium.webdriver.common.by import By


class ProductList:
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@class="btn_primary btn_inventory"]')
    REMOVE_BUTTON = (By.XPATH, '//*[@class="btn_secondary btn_inventory"]')

    LEFT_MENU_BUTTON = (
        By.CSS_SELECTOR,
        "#menu_button_container > div > div:nth-child(3) > div > button",
    )

    ADD_TO_CART_BUTTON_XPATH = ".//div[3]/button"

    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM = (By.CLASS_NAME, "inventory_item")
    ITEMS_LIST = (By.CLASS_NAME, "inventory_list")
    SORT_NAME_A_Z = (
        By.CSS_SELECTOR,
        "#inventory_filter_container > select > option:nth-child(1)",
    )
    SORT_NAME_Z_A = (
        By.CSS_SELECTOR,
        "#inventory_filter_container > select > option:nth-child(2)",
    )
    SORT_PRICE_LOW_HIGH = (
        By.CSS_SELECTOR,
        "#inventory_filter_container > select > option:nth-child(3)",
    )
    SORT_PRICE_HIGH_LOW = (
        By.CSS_SELECTOR,
        "#inventory_filter_container > select > option:nth-child(4)",
    )
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#inventory_filter_container > select")

    HEADER = (By.CLASS_NAME, "product_label")
