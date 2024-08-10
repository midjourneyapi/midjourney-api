import csv
import http.client
import json
import time
import requests
from PIL import Image
from io import BytesIO
import threading


# 设置基础URL和端点
BASE_URL = "midjourncy.com"
SUBMIT_ENDPOINT = "/mj-relax/mj/submit/imagine"
FETCH_ENDPOINT_TEMPLATE = "/mj-relax/mj/task/{task_id}/fetch"

# 设置请求头
headers = {
    'Authorization': 'Bearer sk-B86OuXGCq9mIiFI74fE725040b4d41469f88426178A1454f',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

def submit_task(prompt):
    """
    提交任务到API，生成图像。
    :param prompt: 生成图像的提示词
    :return: 返回任务ID，如果提交失败返回None
    """
    payload = {
        "prompt": prompt
    }
    payload_json = json.dumps(payload)

    try:
        conn = http.client.HTTPSConnection(BASE_URL)
        conn.request("POST", SUBMIT_ENDPOINT, payload_json, headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()
        response_json = json.loads(data.decode("utf-8"))
        if response_json.get('code') == 1:
            task_id = response_json.get("result")
            print(f"Task submission response for prompt '{prompt}': {response_json}")  # 调试信息
            return task_id
        else:
            print(f"Error submitting task for prompt '{prompt}': {response_json.get('description')}")
            return None
    except Exception as e:
        print(f"Error submitting task for prompt '{prompt}': {e}")
        return None

def fetch_task_status(task_id):
    """
    查询任务的状态。
    :param task_id: 任务ID
    :return: 返回任务状态的JSON数据，如果查询失败返回None
    """
    try:
        fetch_endpoint = FETCH_ENDPOINT_TEMPLATE.format(task_id=task_id)
        conn = http.client.HTTPSConnection(BASE_URL)
        conn.request("GET", fetch_endpoint, '', headers)
        res = conn.getresponse()
        data = res.read()
        conn.close()
        fetch_response_json = json.loads(data.decode("utf-8"))
        print(f"Fetch response for task_id '{task_id}': {fetch_response_json}")  # 调试信息
        return fetch_response_json
    except Exception as e:
        print(f"Error fetching task status for task_id '{task_id}': {e}")
        return None

def save_and_split_image(image_url, base_filename):
    """
    下载图像并切割为4张独立的图像。
    :param image_url: 图像URL
    :param base_filename: 基础文件名，用于保存切割后的图像
    """
    try:
        # 下载图像
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        
        # 获取图像尺寸
        width, height = image.size
        
        # 计算每张子图的尺寸
        sub_width = width // 2
        sub_height = height // 2
        
        # 切割图像并保存
        for i in range(2):
            for j in range(2):
                left = j * sub_width
                upper = i * sub_height
                right = left + sub_width
                lower = upper + sub_height
                
                sub_image = image.crop((left, upper, right, lower))
                sub_image_filename = f"{base_filename}_part_{i * 2 + j + 1}.png"
                sub_image.save(sub_image_filename)
                print(f"Saved {sub_image_filename}")

    except Exception as e:
        print(f"Error saving and splitting image: {e}")

def process_prompt(prompt):
    """
    处理单个prompt的任务提交和状态查询。
    :param prompt: 生成图像的提示词
    """
    task_id = submit_task(prompt)

    if task_id:
        print(f"Task submitted successfully with ID: {task_id}")  # 调试信息
        max_retries = 30  # 增加重试次数
        retry_interval = 30  # 增加查询间隔时间

        while True:
            fetch_response_json = fetch_task_status(task_id)
            if fetch_response_json:
                print(f"Fetch response for prompt '{prompt}':", fetch_response_json)

                if fetch_response_json.get("status") == "SUCCESS":
                    print("Task completed for prompt:", prompt)
                    image_url = fetch_response_json.get("imageUrl")
                    if image_url:
                        print("Image URL:", image_url)

                        # 生成图像的基本文件名
                        base_filename = f"{prompt[:30].replace(' ', '_')}"

                        # 下载并切割图像
                        save_and_split_image(image_url, base_filename)
                        break
                elif fetch_response_json.get("status") == "FAILED":
                    print(f"Task for prompt '{prompt}' failed.")
                    break
                else:
                    print(f"Task for prompt '{prompt}' is still in progress.")
            
            time.sleep(retry_interval)
        else:
            print(f"Max retries reached for prompt '{prompt}', task not completed.")
    else:
        print(f"Task submission failed for prompt '{prompt}'.")

def process_prompts(csv_file):
    """
    处理CSV文件中的每个prompt，提交任务并下载生成的图像。
    :param csv_file: CSV文件路径
    """
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        prompts = [row['prompt'] for row in reader]
    
    threads = []
    for prompt in prompts:
        # 创建并启动线程
        thread = threading.Thread(target=process_prompt, args=(prompt,))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

# 调用处理函数
process_prompts('prompts.csv')
