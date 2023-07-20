import time
import os,sys
sys.path.append(os.getcwd())

from base.get_logger import GetLogger
from base.base_driver import init_driver
from page.page import Page

import pytest

# 获取日志入口
log = GetLogger().get_logger()


class TestOpenCarcenter:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        # 等待广告
        time.sleep(5)

    def teardown(self):
        self.driver.quit()

    def test_open_carcenter(self):
        # home - 点击 车辆
        self.page.carcenter.click_carcenter() 
        # 车辆页面 - 判断 更新状态
        assert "能源管理" == self.page.carcenter.get_carcenter_txt()
        log.info("打开车辆，更新状态断言成功")
