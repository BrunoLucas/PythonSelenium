# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class InserirComentario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.google.com.br/"

    def test_inserir_comentario(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("vida de testador")
        driver.find_element_by_link_text("Vida de Testador").click()
        driver.find_element_by_link_text(u"Resolvendo problemas"
                                         u" de versões antigas e novas do Selenium com Gradle + Java").click()
        driver.find_element_by_css_selector("#previewHolder > div.top > img.close").click()
        driver.find_element_by_css_selector("#postCommentButtonHolder > #postCommentSubmit").click()
        driver.find_element_by_css_selector("div.recaptcha-checkbox-checkmark").click()
        driver.find_element_by_id("postCommentSubmit").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
