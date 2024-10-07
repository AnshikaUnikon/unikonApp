from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from appium_flutter_finder.flutter_finder import FlutterFinder
from selenium.webdriver.support.ui import WebDriverWait
import logging
import flutter


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.finder = FlutterFinder()
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                  ignored_exceptions=[ElementNotSelectableException])
        logging.basicConfig(level=logging.INFO)

    def waitForElement(self, locatorValue, locatorType, index=None):
        locatorType = locatorType.lower()
        try:
            if locatorType == "id":
                element = self.wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            elif locatorType == "class":
                elements = self.wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
                element = elements[index] if index is not None and index < len(elements) else None
            elif locatorType == "ui":
                element = self.wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locatorValue))
            elif locatorType == "xpath":
                element = self.wait.until(lambda x: x.find_element(By.XPATH, locatorValue))
            elif locatorType == "flutter":
                element = self.wait.until(lambda x: x.find_element(self.finder.by_value_key(locatorValue)))
            elif locatorType == "scroll":
                element = self.scrollToElement(locatorValue, "xpath")
            else:
                logging.error(f"Locator type '{locatorType}' not supported.")
                return None

            if element is None:
                raise NoSuchElementException(
                    f"Element not found with locatorType: {locatorType} and locatorValue: {locatorValue}")

            logging.info(f"Element found with locatorType: {locatorType} and locatorValue: {locatorValue}")
            return element
        except Exception as e:
            logging.error(f"Error while waiting for element: {str(e)}")
            return None

    def getElement(self, locatorValue, locatorType, index=None):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType, index)
            if element:
                logging.info(f"Element found with locatorType: {locatorType} and locatorValue: {locatorValue}")
            return element
        except Exception as e:
            logging.error(f"Element not found with locatorType: {locatorType} and locatorValue: {locatorValue} - {str(e)}")
            return None

    def clickElement(self, locatorValue, locatorType, index=None):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType, index)
            if element:
                element.click()
                logging.info(f"Clicked element with locatorType: {locatorType} and locatorValue: {locatorValue}")
        except Exception as e:
            logging.error(f"Unable to click on element with locatorType: {locatorType} and locatorValue: {locatorValue} - {str(e)}")

    def clearElement(self, locatorValue, locatorType, index=None):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType, index)
            if element:
                element.clear()
                logging.info(f"Clear element with locatorType: {locatorType} and locatorValue: {locatorValue}")
        except Exception as e:
            logging.error(f"Unable to clear element with locatorType: {locatorType} and locatorValue: {locatorValue} - {str(e)}")

    def sendText(self, text, locatorValue, locatorType, index=None):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType, index)
            if element:
                element.send_keys(text)
                logging.info(f"Sent text '{text}' to element with locatorType: {locatorType} and locatorValue: {locatorValue}")
        except Exception as e:
            logging.error(f"Unable to send text '{text}' to element with locatorType: {locatorType} and locatorValue: {locatorValue} - {str(e)}")

    def isDisplayed(self, locatorValue, locatorType, index=None):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType, index)
            if element and element.is_displayed():
                logging.info(f"Element with locatorType: {locatorType} and locatorValue: {locatorValue} is displayed")
                return True
            else:
                logging.warning(f"Element with locatorType: {locatorType} and locatorValue: {locatorValue} is not displayed")
                return False
        except Exception as e:
            logging.error(f"Error checking display status of element with locatorType: {locatorType} and locatorValue: {locatorValue} - {str(e)}")
            return False

    def scrollToElement(self, locatorValue, locatorType, max_swipes=25):
        for _ in range(max_swipes):
            try:
                if locatorType == "ui":
                    element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locatorValue)
                else:
                    logging.error(f"Unsupported locator type for scroll: {locatorType}")
                    return None

                if element.is_displayed():
                    return element
            except NoSuchElementException:
                self.scrollDown()
        logging.error(f"Element with locatorValue: {locatorValue} not found after {max_swipes} swipes")
        return None

    def scrollDown(self):
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] // 2
        start_y = window_size['height'] * 3 // 4
        end_y = window_size['height'] // 4

        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def swipeLeftToRight(self, start_x_ratio=0.1, end_x_ratio=0.9, y_ratio=0.4, duration=800):
        window_size = self.driver.get_window_size()
        start_x = int(window_size['width'] * start_x_ratio)
        end_x = int(window_size['width'] * end_x_ratio)
        y = int(window_size['height'] * y_ratio)

        self.driver.swipe(start_x, y, end_x, y, duration)

    def backGesture(self):
        self.driver.back()

