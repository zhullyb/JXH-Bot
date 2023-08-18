import requests
import time

class BilibiliSubscribe:
    def __init__(self, bilibili_user_id,
                 ua='Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36',):
        self.ua = ua
        self.api_url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=' + str(bilibili_user_id)

    def get_latest_video_info(self, request_interval=300):
        now = int(time.time())
        ret = ''
        video_list = requests.get(self.api_url, headers={'User-Agent': self.ua}).json()['data']['list']['vlist']
        for video in video_list:
            if now - int(video['created']) <= request_interval + 1:
                ret += video['title'] + '\n'
                ret += 'https://www.bilibili.com/video/' + video['bvid'] + '\n'
                ret += '发布时间：' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(video['created'])) + '\n'
                ret += '-' * 20 + '\n'
        return ret