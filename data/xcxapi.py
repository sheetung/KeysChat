import requests
import json

def forward_mini_app_message(app_id, to_wxid, xml, cover_img_url, token):
    """
    转发小程序消息
    :param app_id: 设备ID
    :param to_wxid: 好友/群的ID
    :param xml: 文件消息的xml
    :param cover_img_url: 小程序封面图链接
    :param token: X-GEWE-TOKEN
    :return: API返回的响应数据
    """
    url = "http://gewe:2531/message/forwardMiniApp"  # 替换为实际的API域名
    headers = {
        'X-GEWE-TOKEN': token,
        'Content-Type': 'application/json'
    }
    payload = {
        "appId": app_id,
        "toWxid": to_wxid,
        "xml": xml,
        "coverImgUrl": cover_img_url
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# 示例调用
if __name__ == "__main__":
    # 替换为实际的参数值
    app_id = "wx_BrOagaY2AAdgGpaqzZ9B1"
    to_wxid = "52390636373@chatroom"
    xml = """<?xml version="1.0"?>
    <msg>
        <appmsg appid="" sdkver="0">
            <title>👇晒出新年第一杯，点赞赢饮茶月卡</title>
            <des />
            <action />
            <type>33</type>
            <showtype>0</showtype>
            <soundtype>0</soundtype>
            <mediatagname />
            <messageext />
            <messageaction />
            <content />
            <contentattr>0</contentattr>
            <url>https://mp.weixin.qq.com/mp/waerrpage?appid=wxafec6f8422cb357b&amp;type=upgrade&amp;upgradetype=3#wechat_redirect</url>
            <lowurl />
            <dataurl />
            <lowdataurl />
            <appattach>
                <totallen>0</totallen>
                <attachid />
                <emoticonmd5 />
                <fileext />
                <cdnthumburl>3057020100044b30490201000204573515c902032f7d6d020416b7bade020465922a53042437383139393934652d323662652d346430662d396466362d3466303137346139616362390204051408030201000405004c53d900</cdnthumburl>
                <cdnthumbmd5>33cf0a1101e7f8cd3057cd417a691f0b</cdnthumbmd5>
                <cdnthumblength>96673</cdnthumblength>
                <cdnthumbwidth>600</cdnthumbwidth>
                <cdnthumbheight>500</cdnthumbheight>
                <cdnthumbaeskey>6f3098f2ee8b351b6cc9b1818d580356</cdnthumbaeskey>
                <aeskey>6f3098f2ee8b351b6cc9b1818d580356</aeskey>
                <encryver>0</encryver>
            </appattach>
            <extinfo />
            <sourceusername>gh_e9d25e745aae@app</sourceusername>
            <sourcedisplayname>霸王茶姬</sourcedisplayname>
            <thumburl />
            <md5 />
            <statextstr />
            <weappinfo>
                <username><![CDATA[gh_e9d25e745aae@app]]></username>
                <appid><![CDATA[wxafec6f8422cb357b]]></appid>
                <type>2</type>
                <version>193</version>
                <weappiconurl><![CDATA[]]></weappiconurl>
                <pagepath><![CDATA[/pages/page/page.html?code=JKD6DA55_3&channelCode=scrm_t664sgg5mrzxkqa]]></pagepath>
                <shareId><![CDATA[0_wxafec6f8422cb357b_25984983017778987@openim_1704162955_0]]></shareId>
                <pkginfo>
                    <type>0</type>
                    <md5><![CDATA[]]></md5>
                </pkginfo>
                <appservicetype>0</appservicetype>
            </weappinfo>
        </appmsg>
        <fromusername>zhangchuan2288</fromusername>
        <scene>0</scene>
        <appinfo>
            <version>1</version>
            <appname></appname>
        </appinfo>
        <commenturl></commenturl>
    </msg>"""
    cover_img_url = "http://dummyimage.com/400x400"
    token = "6fac0754e60e45feb8a5af382c88380a"  # 替换为你的Token

    response = forward_mini_app_message(app_id, to_wxid, xml, cover_img_url, token)
    print("API Response:", response)