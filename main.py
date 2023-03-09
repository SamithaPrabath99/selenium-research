"""
    This is a main file of this project purpose of this project is improves knowledge about selenium with python
"""
import os
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

YOUTUBE = 'https://www.youtube.com/'
def get_trending_videos(url: str):
    os.environ['PATH'] += os.environ['CHROME_PATH']
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.get(url)

    trending = driver.find_element(By.XPATH, '//a[@title="Trending"]')
    trending.click()

    video_list = driver.find_elements(By.XPATH, '//*[@id="grid-container"]/ytd-video-renderer')
    print('Thumbnail Link | Title | Channel Name | Views | Days | Video Link')
    for video in video_list:
        driver.execute_script("arguments[0].scrollIntoView();", video)
        image = video.find_element(By.TAG_NAME, 'img')
        print(image.get_attribute('src'), end=' | ')

        title = video.find_element(By.TAG_NAME, 'yt-formatted-string')
        print(title.text, end=' | ')

        channel_name = video.find_element(By.XPATH, r'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div['
                                                    r'1]/ytd-channel-name/div/div/yt-formatted-string/a')
        print(channel_name.text, end=' | ')

        views = video.find_element(By.XPATH, 'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]')
        print(views.text, end=' | ')

        days = video.find_element(By.XPATH, 'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]')
        print(days.text, end=' | ')

        video_url = video.find_element(By.XPATH, 'div[1]/ytd-thumbnail/a')
        print(video_url.get_attribute('href'))

    driver.quit()


def get_search_result(url,keywords):
    pass


def get_user_choice():
    print('Hi There, This is simple youtube scraping testing project \n\n'
          'This project help you to get some information \n\n'
          'First You need to select choice \n'
          'G-give the keyword to search\n'
          'O-automation and give me trending video details\n\n'
          'enter for exit')
    while True:
        choice = input('Please Enter your choice').upper()

        if choice == 'G':
            keywords = input('what do you want to search ? ')
            get_search_result(YOUTUBE,keywords=keywords)
        elif choice == 'O':
            get_trending_videos(YOUTUBE)
        else:
            break
