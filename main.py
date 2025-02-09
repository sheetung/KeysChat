from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import *

# 注册插件
@register(name='KeywordTrigger', 
          description='关键词触发插件', 
          version='0.11', 
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
        if "云服务器" in msg:
            sender_id = ctx.event.sender_id
            # 构建要发送的消息
            message = [
                At(target=sender_id),  # At发送者
                "\n云服务器9.9/年，只圈钱不跑路\n"
            ]
            # 添加图片
            image_url = "https://static.moontung.top/2024/202409021559544.jpg"  # 替换为实际的图片URL
            message.append(Image(url=image_url))

            # 发送消息
            await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id), MessageChain(message))
            ctx.prevent_default()
            ctx.prevent_postorder()

    # 插件卸载时触发
    def __del__(self):
        pass