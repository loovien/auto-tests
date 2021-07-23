# -*- coding: utf-8 -*-
# website: https://loovien.github.io
# author: luowen<bigpao.luo@gmail.com>
# time: 2018/9/29 21:41
# desc:

import os
from typing import Any, Dict, Optional


def PATH(p: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', p))


def get_desired_capabilities(app: Optional[str] = None) -> Dict[str, Any]:
    desired_caps: Dict[str, Any] = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'newCommandTimeout': 240,
        'automationName': 'UIAutomator2',
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000,
        'app': ""
    }

    if app is not None:
        desired_caps['app'] = PATH(os.path.join('../', '', app))

    return desired_caps
