from config.config import BASE_URL


def test_launch(driver):

    driver.get(BASE_URL)

    assert "Tichi" in driver.title