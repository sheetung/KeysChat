import json
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import *
import os

# 注册插件
@register(name='KeysChat', 
          description='关键词触发插件', 
          version='0.13', 
          author="sheetung")
class KeywordTriggerPlugin(BasePlugin):
    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    @handler(PersonMessageReceived)
    @handler(GroupMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = str(ctx.event.message_chain).strip()
        sender_id = ctx.event.sender_id
        # print(f'ys={ctx.event.message_event}')
        # 每次收到消息时加载 JSON 文件
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'keyword_responses.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            keyword_responses = json.load(f)

        # 检查消息中是否包含关键词
        for keyword, response in keyword_responses.items():
            if keyword in msg:
                # 构建要发送的消息
                message = [
                    At(target=sender_id),  # At发送者
                    "\n",
                    response["message"],  # 回复消息
                    "\n"
                ]
                # 添加图片
                if response["image_url"]:
                    message.append(Image(url=response["image_url"]))

                # 发送消息
                await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id), MessageChain(message))
                ctx.prevent_default()
                ctx.prevent_postorder()
                break  # 匹配到一个关键词后退出循环

    # 插件卸载时触发
    def __del__(self):
        pass
