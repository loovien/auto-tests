# -*- coding: utf-8 -*-
# website: https://loovien.github.io
# author: luowen<bigpao.luo@gmail.com>
# time: 2018/9/29 21:41
# desc:

import base64
import os

from unittest import TestCase
from configs import GLOBAL
from appium import webdriver
from helper import is_ci

from . import desired_capabilities


class BaseTestCase(TestCase):
    def setup_method(self, method) -> None:  # type: ignore
        desired_caps = desired_capabilities.get_desired_capabilities(GLOBAL.get("apk", "lt-sports.apk"))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        if is_ci():
            self.driver.start_recording_screen()

    def teardown_method(self, method) -> None:  # type: ignore
        if is_ci():
            payload = self.driver.stop_recording_screen()
            video_path = os.path.join(os.getcwd(), method.__name__ + '.mp4')
            with open(video_path, "wb") as fd:
                fd.write(base64.b64decode(payload))
        self.driver.quit()
