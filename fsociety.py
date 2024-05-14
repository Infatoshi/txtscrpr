from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import subprocess
import json
import os

# Initialize WebDriver
driver = webdriver.Chrome()
first_n_results = 5

def init_directories(topics):
    for topic in topics:
        dir_path = os.path.join(os.getcwd(), "topics", topic)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory for: {topic}")
        for subtopic in topics[topic]:
            subtopic_path = os.path.join(dir_path, subtopic)
            if not os.path.exists(subtopic_path):
                os.makedirs(subtopic_path)
                print(f"Created directory for: {subtopic}")


def delete_small_files(directory, size_limit=500*1024):  # 500KB limit
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) < size_limit:
                os.remove(file_path)
                print(f"Deleted small file: {file_path}")
def find_resume_point(topics):
    for topic in topics:
        for subtopic in topics[topic]:
            subtopic_path = os.path.join(os.getcwd(), "topics", topic, subtopic)
            if os.listdir(subtopic_path):  # Check if directory is not empty
                continue
            return topic, subtopic
    return None, None

driver.get('http://www.google.com')
time.sleep(2)

with open('topics.json') as f:
    topics = json.load(f)
    init_directories(topics)

topic_to_resume, subtopic_to_resume = find_resume_point(topics)

resume = False
for topic in topics:
    for subtopic in topics[topic]:
        if topic_to_resume and subtopic_to_resume:
            if topic == topic_to_resume and subtopic == subtopic_to_resume:
                resume = True
            if not resume:
                continue

        print(f"Searching for textbooks on: {subtopic}")
        query = driver.find_element(By.NAME, 'q')
        query.clear()
        query.send_keys(f'{subtopic} textbook filetype:pdf')
        query.send_keys(Keys.RETURN)
        time.sleep(5)

        pdf_links = []
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        for element in elements[:first_n_results]:
            links = element.find_elements(By.CSS_SELECTOR, 'a')
            for link in links:
                href = link.get_attribute('href')
                if href and '.pdf' in href:
                    local_path = f"topics/{topic}/{subtopic}/{os.path.basename(href)}"
                    if not os.path.exists(local_path):
                        print(f"Downloading PDF from: {href}")
                        subprocess.run(['wget', '--tries=1', '-nc', '-P', f"topics/{topic}/{subtopic}", href])
                        time.sleep(1)  # Small pause to prevent rapid-fire requests

driver.quit()

# After all downloads, delete small files
for topic in topics:
    topic_path = os.path.join(os.getcwd(), "topics", topic)
    delete_small_files(topic_path)
