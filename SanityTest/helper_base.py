import os
import time
import unittest
from lib2to3.pgen2 import driver
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pynput.keyboard import Key
from SanityTest.shared_elements import SharedElements
from SanityTest.select_by import SelectBy
from SanityTest.action import Action
from SanityTest.driver_instanse import Driver
from selenium.common.exceptions import NoSuchElementException
from SanityTest.test_name import TestNames
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class HelperBase:
    WAIT_TIME = 7
    NUM_OF_TRIES = 3

    @staticmethod
    def get_driver_and_configure_browser_and_url(url, is_headless, reset):
        return Driver(url, reset)

    @staticmethod
    def login_to_commbox(brand, username, password):
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_COMPANY_NAME, Action.SEND_KEYS, brand)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.CONTINUE_BUTTON, Action.CLICK)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_EMAIL, Action.SEND_KEYS, username)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_PASSWORD, Action.SEND_KEYS, password)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_BUTTON, Action.CLICK)
        #HelperBase.close_browser_window()

    @staticmethod
    def sending_email_from_mange(brand, username, password, self):
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_COMPANY_NAME, Action.SEND_KEYS, brand)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.CONTINUE_BUTTON, Action.CLICK)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_EMAIL, Action.SEND_KEYS, username)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_PASSWORD, Action.SEND_KEYS, password)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.LOGIN_BUTTON, Action.CLICK)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.COMPOSE_BUTTON, Action.CLICK)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.CLICK_ON_STREAM, Action.CLICK)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.TO_TEXT_FIELD, Action.SEND_KEYS, "ran.ya@commbox.io")
        HelperBase.action_on_element(SelectBy.ID, SharedElements.SUBJECT_TEXT_FIELD, Action.SEND_KEYS, "Automation test")
        #HelperBase.action_on_element(SelectBy.XPATH, SharedElements.TIMEING_MESSAGE_BUTTON, Action.SCROLL_DOWN)
        time.sleep(2)
        HelperBase.action_on_element(SelectBy.ID, SharedElements.SEND_BUTTON, Action.CLICK)
        # N = 2
        # actions = ActionChains(driver)
        # for _ in range(N):
        #     actions = actions.send_keys(Keys.TAB)
        # actions.perform()


    @staticmethod
    def select_element_by_type(select_by, selector):
        driver = Driver().get_driver()
        selected_element = None
        try:
            if select_by is SelectBy.ID:
                selected_element = driver.find_element_by_id(selector)
            elif select_by is SelectBy.XPATH:
                selected_element = driver.find_element_by_xpath(selector)
            elif select_by is SelectBy.CSS_SELECTOR:
                selected_element = driver.find_element_by_css_selector(selector)
            elif select_by is SelectBy.CLASS_NAME:
                selected_element = driver.find_element_by_class_name(selector)
            elif select_by is SelectBy.TAG_NAME:
                selected_element = driver.find_element_by_tag_name(selector)




        except:
            return None
        else:
            return selected_element

    @staticmethod
    def action_on_element(select_by, selector, action, text=''):
        selected_element = None
        try_counter = 0
        is_clickable = False

        while not (is_clickable) and (try_counter < HelperBase.NUM_OF_TRIES):
            try:
                selected_element = HelperBase.select_element_by_type(select_by, selector)
                selected_element.click()

                if action is Action.SEND_KEY_WITH_CLEAR:
                    selected_element.clear()
                if action is Action.SEND_KEYS or action is Action.SEND_KEY_WITH_CLEAR:
                    selected_element.send_keys(text)
                if action is Action.VISIBILITY_OFF:
                    selected_element.is_displayed()
                if action is Action.SEND_KEYS_WITH_TAB:
                    ActionChains(action).send_keys(Keys.TAB * 2).perform()
                if action is Action.SCROLL_DOWN:
                    selected_element.location_once_scrolled_into_view()


                is_clickable = True

            except:
                time.sleep(HelperBase.WAIT_TIME)
                try_counter += 1
               # exception_message = ValueError

        if try_counter == HelperBase.NUM_OF_TRIES:
            selected_element = None
            print("some error occurred")
            raise Exception('Element not found')


        return selected_element

    @staticmethod
    def print_starting_message(output_message):
        print('\n' + output_message)

    @staticmethod
    def refresh():
        driver = Driver().get_driver()
        driver.refresh()

    @staticmethod
    def close_browser_window():
        driver = Driver()
        driver.close_driver()
        del driver

    @staticmethod
    def get_title(self):
        header_title = self.driver.find_element_by_ID("tabBtn_1").text
        self.assertEqual(header_title, "שיחות", "Title is wrong")

