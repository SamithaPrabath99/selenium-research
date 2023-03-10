"""
    This is a main file of this project purpose of this project is improves knowledge about selenium with python
"""
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


YOUTUBE = 'https://www.youtube.com/'


def setup_browser():
    os.environ['PATH'] += os.environ['CHROME_PATH']
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(60)
    return driver


def get_trending_videos(url=YOUTUBE):
    details = list()
    driver = setup_browser()
    driver.get(url)

    trending = driver.find_element(By.XPATH, '//a[@title="Trending"]')
    trending.click()

    video_list = driver.find_elements(By.XPATH, '//*[@id="grid-container"]/ytd-video-renderer')
    print('Thumbnail Link | Title | Channel Name | Views | Days | Video Link')
    data = {}
    for video in video_list:
        driver.execute_script("arguments[0].scrollIntoView();", video)
        image = video.find_element(By.TAG_NAME, 'img')
        print(image.get_attribute('src'), end=' | ')
        data['thumbnail-url'] = image.get_attribute('src')

        title = video.find_element(By.TAG_NAME, 'yt-formatted-string')
        print(title.text, end=' | ')
        data['title'] = title.text

        channel_name = video.find_element(By.XPATH, r'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div['
                                                    r'1]/ytd-channel-name/div/div/yt-formatted-string/a')
        print(channel_name.text, end=' | ')
        data['channel_name'] = channel_name.text

        views = video.find_element(By.XPATH, 'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]')
        print(views.text, end=' | ')
        data['views'] = views.text

        days = video.find_element(By.XPATH, 'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]')
        print(days.text, end=' | ')
        data['days'] = days.text

        video_url = video.find_element(By.XPATH, 'div[1]/ytd-thumbnail/a')
        print(video_url.get_attribute('href'))
        data['video-url'] = video_url.get_attribute('href')
        details.append(data)
        data = {}
    driver.quit()
    return details


def get_search_result(url=YOUTUBE, keywords='test'):
    details = list()
    if keywords == '':
        keywords = 'test'
    driver = setup_browser()
    driver.get(url+f'results?search_query={keywords}')

    video_list = driver.find_elements(By.XPATH, '//*[@id="contents"]/ytd-video-renderer')
    print(video_list)
    print('Thumbnail Link | Title | Channel Name | Views | Days | Video Link')
    data = {}
    for video in video_list:
        driver.execute_script("arguments[0].scrollIntoView();", video)
        image = video.find_element(By.TAG_NAME, 'img')
        print(image.get_attribute('src'), end=' | ')
        data['thumbnail-url'] = image.get_attribute('src')

        title = video.find_element(By.TAG_NAME, 'yt-formatted-string')
        print(title.text, end=' | ')
        data['title'] = title.text

        channel_name = video.find_element(By.XPATH, 'div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a')
        print(channel_name.text, end=' | ')
        data['channel_name'] = channel_name.text

        views = video.find_element(By.XPATH, 'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]')
        print(views.text, end=' | ')
        data['views'] = views.text

        days = video.find_element(By.XPATH, 'div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]')
        print(days.text, end=' | ')
        data['days'] = days.text

        video_url = video.find_element(By.XPATH, 'div[1]/ytd-thumbnail/a')
        print(video_url.get_attribute('href'))
        data['video-url'] = video_url.get_attribute('href')
        details.append(data)
        data = {}

    driver.quit()
    return details


def get_user_choice():
    print('Hi There, This is simple youtube scraping testing project \n\n'
          'This project help you to get some information \n\n'
          'First You need to select choice \n\n'
          'G-give the keyword to search\n'
          'O-automation and give me trending video details\n'
          'enter for exit\n\n')
    while True:
        choice = input('Please Enter your choice : ').upper()

        if choice == 'G':
            keywords = input('what do you want to search ?   ')
            get_search_result(YOUTUBE, keywords=keywords)
        elif choice == 'O':
            get_trending_videos(YOUTUBE)
        else:
            break
