from django.test.testcases import TestCase
from SuiSiannAdminApp.models import 文章表, 句表
from SuiSiannAdminApp.management.commands.重錄後更新音檔所在 import 更新音檔所在
from unittest import mock
from django.core.management import call_command
from os.path import os, dirname


class 更新音檔所在單元試驗(TestCase):

    @mock.patch(
        'SuiSiannAdminApp.management.commands.重錄後更新音檔所在.更新音檔所在')
    def test_有傳入參數(self, 更新音檔所在):
        call_command('重錄後更新音檔所在', os.path.join(dirname(__file__), './NG句_test.csv'))
        更新音檔所在.assert_any_call('1', '若以早我', 'Mar 16, 2019_220.wav')

    def test_改著一筆(self):
        整句漢字 = "若以早我真厚話，愛我起攔頭"
        這句 = 句表.objects.create(
            來源=文章表.objects.create(文章名='33'),
            音檔="Oct 8, 1.wav",
            漢字=整句漢字,
            原始漢字=整句漢字,
            羅馬字含口語調="a",
            原始羅馬字="a",
        )
        這句.full_clean()
        這句.save()
        更新音檔所在('1', '若以早我', 'Mar 16, 2019_1.wav')
        音檔所在 = 句表.objects.get(pk=這句.pk).音檔
        self.assertEqual(音檔所在, "Mar 16, 2019_1.wav")
