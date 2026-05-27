# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import json

from typing import List

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> ocr_api20210707Client:
        """
        匿名方式初始化账号Client
        @return: Client
        @throws Exception
        """
        # 支持匿名访问的 API，不需要 AccessKey ID 等鉴权配置。
        # 更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config()
        # Endpoint 请参考 https://api.aliyun.com/product/ocr-api
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        recognize_edu_paper_cut_request = ocr_api_20210707_models.RecognizeEduPaperCutRequest(
            cut_type='question',
            image_type='photo',
            subject='Physics'
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.recognize_edu_paper_cut_with_options(recognize_edu_paper_cut_request, runtime)
            print(json.dumps(resp, default=str, indent=2))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        recognize_edu_paper_cut_request = ocr_api_20210707_models.RecognizeEduPaperCutRequest(
            cut_type='question',
            image_type='photo',
            subject='Physics'
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = await client.recognize_edu_paper_cut_with_options_async(recognize_edu_paper_cut_request, runtime)
            print(json.dumps(resp, default=str, indent=2))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
