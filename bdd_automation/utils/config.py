import os

class Config:
    # Base URL for Magento site
    BASE_URL = "https://magento.softwaretestingboard.com"

    # Paths
    SCREENSHOT_PATH = os.path.join(os.getcwd(), "screenshots")

    # Test credentials
    VALID_EMAIL = "validuser@gmail.com"
    VALID_PASSWORD = "Test@1234"
    INVALID_EMAIL = "invaliduser@gmail.com"
    INVALID_PASSWORD = "WrongPass@123"

    # Browser settings
    BROWSER = "chrome"  # Change to 'firefox' if needed

    @staticmethod
    def get_driver_path():
        """Returns the WebDriver path based on OS."""
        return os.path.join(os.getcwd(), "drivers", "chromedriver")

