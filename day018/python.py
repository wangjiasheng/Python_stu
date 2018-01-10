#! -*- coding:utf-8 -*-
import jieba
seg_list = jieba.cut("北京野生动物园轿车遭黑熊围堵")
print "Default Mode:", ' '.join(seg_list)


seg_list = jieba.cut("我叫王家胜", cut_all=False)
print("Precise Mode: " + "/".join(seg_list))  # 精确模式，默认状态下也是精确模式