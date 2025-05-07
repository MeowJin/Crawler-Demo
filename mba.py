import os
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from tqdm import tqdm


def getVideo():
    cookies = {
        '_gcl_au': '1.1.1166628955.1745904987',
        '_ga': 'GA1.1.1715576345.1745904987',
        'wikidb_session': 'r080mcmg84l40lpc6514ev6rb0',
        'Hm_lvt_1c51a09d54b2f6aeb599844163d86610': '1745904990',
        'HMACCOUNT': '3F202E2A0B724E90',
        'wikidbweixininfo': '__',
        'wikidbLoginToken': 'eyJ0aW1lIjoxNzQ4NDk3MDQ0LCJ0eXBlIjoiYWNjb3VudCIsInVzZXJuYW1lIjoiTV9pZF8zZTI1NzM2MmQyN2UyYmRhYzZhMjU4MTVmYjY1Yjg4NyIsImtleSI6ImJkZDQxOTgyYWQ5MWZiMjkwNzg3NGIwMGIzOWQ4MjQ0In0%3D',
        'wikidbLoginId': '30232181745905044',
        'wikidbUserName': 'M_id_3e257362d27e2bdac6a25815fb65b887',
        'wikidbNickName': 'Lena',
        'wikidbAccessToken': 'eyJ1c2VybmFtZSI6Ik1faWRfM2UyNTczNjJkMjdlMmJkYWM2YTI1ODE1ZmI2NWI4ODciLCJ0aW1lIjoxNzQ1OTA4NjQ0LCJrZXkiOiI4Mzg5YjRkZDhmZGM4YjBjN2NhMjBjNDU5MzVmZDY1YSJ9',
        '_ga_NERG9FCK5N': 'GS1.1.1745904986.1.1.1745905130.59.0.1496429603',
        'Hm_lpvt_1c51a09d54b2f6aeb599844163d86610': '1745905133',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,sq;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_gcl_au=1.1.1166628955.1745904987; _ga=GA1.1.1715576345.1745904987; wikidb_session=r080mcmg84l40lpc6514ev6rb0; Hm_lvt_1c51a09d54b2f6aeb599844163d86610=1745904990; HMACCOUNT=3F202E2A0B724E90; wikidbweixininfo=__; wikidbLoginToken=eyJ0aW1lIjoxNzQ4NDk3MDQ0LCJ0eXBlIjoiYWNjb3VudCIsInVzZXJuYW1lIjoiTV9pZF8zZTI1NzM2MmQyN2UyYmRhYzZhMjU4MTVmYjY1Yjg4NyIsImtleSI6ImJkZDQxOTgyYWQ5MWZiMjkwNzg3NGIwMGIzOWQ4MjQ0In0%3D; wikidbLoginId=30232181745905044; wikidbUserName=M_id_3e257362d27e2bdac6a25815fb65b887; wikidbNickName=Lena; wikidbAccessToken=eyJ1c2VybmFtZSI6Ik1faWRfM2UyNTczNjJkMjdlMmJkYWM2YTI1ODE1ZmI2NWI4ODciLCJ0aW1lIjoxNzQ1OTA4NjQ0LCJrZXkiOiI4Mzg5YjRkZDhmZGM4YjBjN2NhMjBjNDU5MzVmZDY1YSJ9; _ga_NERG9FCK5N=GS1.1.1745904986.1.1.1745905130.59.0.1496429603; Hm_lpvt_1c51a09d54b2f6aeb599844163d86610=1745905133',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://ke.mbalib.com/pc/column/37?tabId=3&id=144',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        't': '1745905133',
        'id': '37',
        'access_token': 'eyJ1c2VybmFtZSI6Ik1faWRfM2UyNTczNjJkMjdlMmJkYWM2YTI1ODE1ZmI2NWI4ODciLCJ0aW1lIjoxNzQ1OTA4NjQ0LCJrZXkiOiI4Mzg5YjRkZDhmZGM4YjBjN2NhMjBjNDU5MzVmZDY1YSJ9',
        'type': 'all',
        'task': '1',
    }

    response = requests.get('https://ke.mbalib.com/api/getColumnCourse', params=params, cookies=cookies,
                            headers=headers)
    return response


def sanitize_filename(name):
    """清理文件名中的非法字符"""
    return ''.join(c if c.isalnum() or c in (' ', '.', '_') else '_' for c in name)


def download_video(url, filename, chunk_size=1024 * 10):
    """下载视频并显示进度条"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))

        with open(filename, 'wb') as f, tqdm(
                desc=os.path.basename(filename),
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                leave=False
        ) as bar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
        return True, filename
    except Exception as e:
        print(f"❌ 下载失败: {filename} | 错误: {e}")
        return False, filename


def process_item(item, chapter_dir):
    title = sanitize_filename(item['title'])
    video_url = item['original_source']
    filename = os.path.join(chapter_dir, f"{title}.mp4")

    if os.path.exists(filename):
        print(f"⏩ 已存在: {title}.mp4")
        return False, filename

    print(f"⬇️ 开始下载: {title}")
    success, file = download_video(video_url, filename)
    if success:
        print(f"✅ 完成: {title}.mp4")
    else:
        print(f"❗ 下载中断或失败: {title}.mp4")
    return success, file


def downloadVideo(json_data, base_dir="downloaded_videos", max_workers=5):
    """主函数：解析JSON并开始下载"""
    data = json.loads(json_data) if isinstance(json_data, str) else json_data
    courses = data['data']

    os.makedirs(base_dir, exist_ok=True)

    for course in courses:
        chapter_title = sanitize_filename(course['title'])
        chapter_dir = os.path.join(base_dir, chapter_title)
        os.makedirs(chapter_dir, exist_ok=True)

        print(f"\n📁 正在处理章节：{chapter_title}")

        materials = course.get('material_list', [])

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(process_item, item, chapter_dir): item for item in materials}

            for future in as_completed(futures):
                try:
                    success, filename = future.result()
                except Exception as exc:
                    print(f'生成器引发了一个异常: {exc}')


if __name__ == '__main__':
    respJson = getVideo()
    downloadVideo(respJson.json())

