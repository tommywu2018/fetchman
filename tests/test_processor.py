#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest2 as unittest
from fetchman.processor.test_processor import Tuliu_Processor
from fetchman.spider.spider_core import SpiderCore
from fetchman.pipeline.console_pipeline import ConsolePipeline
from fetchman.pipeline.test_pipeline import TestPipeline


class TestProcessor(unittest.TestCase):
    def test_car_processor(self):
        test_pipeline = TestPipeline()
        SpiderCore(Tuliu_Processor(),test=True).set_pipeline(ConsolePipeline(),'console')\
            .set_pipeline(test_pipeline,'test').start()
        self.assertIn('2018',"2018-01-07 09:40:39")
