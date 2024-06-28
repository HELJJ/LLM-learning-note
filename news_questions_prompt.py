# -*-coding:utf-8 -*-
"""
# File       : news_questions_prompt.py
# Time       ：2024/6/4 17:12
# Author     ：lz
# Description：
"""
NEWS_QUESTIONS_PROMPT = """
你是一个新闻问题生成器，给你一篇新闻文章的标题和内容，你需要生成相关中文问题。
要求：
1、问题不超过5个
以json对象形式回复，'questions'为键，生成的问题列表为值。
文章标题：{title}
文章内容：{content}
"""