import os
import sys
import json

from typing import List

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

root_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(root_dir, "output")


#  Math:数学,  Chinese:语文,  English:英语, Physics:物理, Chemistry: 化学, Biology:生物,  History:历史,  Geography:地理, Politics:政治
image_info = [
    {'url': 'https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(1).jpg', 'subject': 'Physics'},
    {'url': 'https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(2).jpg', 'subject': 'Math'},
    {'url': 'https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(3).jpg', 'subject': 'History'},
    {'url': 'https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(4).jpg', 'subject': 'Math'},
    {'url': 'https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(5).jpg', 'subject': 'Math'},
    {'url': 'https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(6).jpg', 'subject': 'Math'}
]

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

        config = open_api_models.Config(
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'

        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        list_scan: List[str],
    ) -> None:
        """
         识别指定图片的题目并切题
         """

        client = Sample.create_client()
        runtime = util_models.RuntimeOptions()

        print(f"{'-'*50}")
        print(f"开始识别图片...")
        print(f"{'-'*50}")

        for i in list_scan:
            recognize_edu_paper_cut_request = ocr_api_20210707_models.RecognizeEduPaperCutRequest(
                url=image_info[i-1]['url'],
                cut_type='question',
                image_type='photo',
                subject=image_info[i-1]['subject']
            )
            print(f"正在识别第{i}张图片...")
            try:
                resp = client.recognize_edu_paper_cut_with_options(recognize_edu_paper_cut_request, runtime)

                save_path = os.path.join(save_dir, f'第{i}张图片的识别结果.json')
                with open(save_path,'w', encoding='utf-8') as f:
                    json.dump(resp.to_map(), f, ensure_ascii=False, indent=2)
                print(f"第{i}张图片识别完成，结果已保存至{save_path}")

            except Exception as error:
                print(f"第{i}张图片识别失败，错误信息如下：")
                # 错误 message
                print(error.message)
                # 诊断地址
                print(error.data.get("Recommend"))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        """
        并行切题接口
        """

        client = Sample.create_client()
        recognize_edu_paper_cut_request = ocr_api_20210707_models.RecognizeEduPaperCutRequest(
            url='https://cdn.jsdelivr.net/gh/DRKing307/Intelligent-Homework-Grading-System@main/datas/1%20(1).jpg',
            cut_type='question',
            image_type='photo',
            subject='Physics'
        )
        runtime = util_models.RuntimeOptions()
        try:
            #切题
            resp = await client.recognize_edu_paper_cut_with_options_async(recognize_edu_paper_cut_request, runtime)
            print(json.dumps(resp, default=str, indent=2))
        except Exception as error:
            #错误处理
            print(error.message)
            print(error.data.get("Recommend"))


if __name__ == '__main__':
    print(f"请输入要识别的图片的编号(输入-1结束):")
    list_scan = []
    while True:
        index = input()
        try:
            index = int(index)
            if index == -1:
                break
            if index < 1 or index > 6:
                print(f"请输入1-6的数字")
                continue
            list_scan.append(index)
        except:
            print(f"请输入数字")
            continue
    Sample.main(list_scan)
    
