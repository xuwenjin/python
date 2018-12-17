#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#爬虫-网页解析器

from bs4 import BeautifulSoup
import urlparse, re

class HtmlParser(object):

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item"));
        for link in links:
            new_url = link['href']
            #urlparse.urljoin: new_url根据url格式，自动拼接
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_data = {}

        res_data['url'] = url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data
