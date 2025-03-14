import json
import random  # 导入 random 模块
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import *
import pkg.platform.types as platform_types
import os

# 注册插件
@register(name='KeysChat', 
          description='关键词触发插件', 
          version='0.13', 
          author="sheetung")
class KeywordTriggerPlugin(BasePlugin):
    # 插件加载时触发
    def __init__(self, host: APIHost):
        self.host = host

    # @handler(PersonMessageReceived)
    @handler(GroupMessageReceived)
    # @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = str(ctx.event.message_chain).strip()
        sender_id = ctx.event.sender_id
        # print(f'ctx.event.launcher_id={ctx.event.launcher_id}')
        print(f'sender_id={sender_id}')
        # 每次收到消息时加载 JSON 文件
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'keyword_responses.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            keyword_responses = json.load(f)

        # 检查消息中是否包含关键词
        for keyword, response in keyword_responses.items():
            if keyword in msg:
                # 构建要发送的消息
                messages = [platform_message.Plain(text=response["description"]),]
                # 添加图片
                if response["urls"]:
                    # 随机选择一个图片URL
                    random_image_url = random.choice(response["urls"])
                    messages.append(platform_message.Image(url=str(random_image_url)))

                # 发送消息
                print(f'launcher = {ctx.event.launcher_type}')
                # 添加At
                messages.insert(0,platform_message.At(sender_id))
                print(f'msg={messages}')
                print(f'msgC={platform_types.MessageChain(messages)}')
                await ctx.host.send_active_message(
                            adapter=self.host.get_platform_adapters()[0],
                            target_type=str(ctx.event.launcher_type),
                            target_id=str(ctx.event.launcher_id),
                            message=platform_types.MessageChain(messages)
                        )
                # await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id), MessageChain(message))
                ctx.prevent_default()
                ctx.prevent_postorder()
                break  # 匹配到一个关键词后退出循环

    # 插件卸载时触发
    def __del__(self):
        pass
