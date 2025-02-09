from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import *

# 注册插件
@register(name='KeysChat', 
          description='关键词触发插件', 
          version='0.12', 
          author="sheetung")
class KeywordTriggerPlugin(BasePlugin):
    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    @handler(PersonMessageReceived)
    @handler(GroupMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = str(ctx.event.message_chain).strip()
        # 检查是否包含关键词“云服务器”
        sender_id = ctx.event.sender_id

        # 定义关键词与回复内容的映射表
        keyword_responses = {
            "云服务器": {
                "message": "\n云服务器9.9/年，只圈钱不跑路\n",
                "image_url": "https://static.moontung.top/2024/202409021559544.jpg"  # 替换为实际的图片URL
            },
            "优惠活动": {
                "message": "优惠活动开始了，快来抢购！\n5.9/年\n",
                "image_url": "https://static.moontung.top/2024/202409021559544.jpg" 
            },
            "客服": {
                "message": "客服在线，欢迎咨询！",
                "image_url": "" # 没有图片则为空
            }
        }

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