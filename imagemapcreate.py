from linebot.models import ImagemapSendMessage, BaseSize, ImagemapAction, URIImagemapAction, MessageImagemapAction, ImagemapArea

# サンプル追加
import json

FILENAME="imagemap.json"
fd = open(FILENAME, mode='r')
data = json.load(fd)
fd.close()


#サンプル追加

def make_imagemap():
    messages = ImagemapSendMessage(
        base_url=data['baseUrl'],
        alt_text=data['altText'],
        base_size=BaseSize(width=data['baseSize']['width'], height=data['baseSize']['height']),
        actions=[
            URIImagemapAction(
                link_uri=data['actions']['linkUri'],
                area=ImagemapArea(
                    x=0, y=0, width=data['actions']['area']['width'], height=data['actions']['area']['height']
                )
            ),
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(
                    x=520, y=0, width=1040, height=605
                )
            )
        ]
    )
    return messages