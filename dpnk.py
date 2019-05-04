import os, sys

try:
    import discord
except:
    print("Discord 모듈을 찾을 수 없습니다!")
    os.system("pip install discord")
    import discord

try:
    import argparse
except:
    print("argparse 모듈을 찾을 수 없습니다!")
    os.system("pip install argparse")
    import argparse

class DPNKException(Exception):
    pass

app = discord.Client()
created_channel = False
create_channel_name = ""
to_send = ""

class DPNKDiscordClient():
    def __init__(self, send, create_channel_names=None):
        app.run(bot_token)

        if create_channel_names is None:
            created_channel = False
        else:
            created_channel = True
            create_channel_name = create_channel_names
        
        to_send = send
    
    @app.event
    async def on_ready():
        Error_guild = []
        notice_channels = []
        success_send = []

        for guild in app.guilds:
            guild_schannel = False

            for channel in guild.channels:
                if "공지" in channel.name or "notice" in channel.name:
                    notice_channels.append(channel)
                    guild_schannel = True
            
            if not guild_schannel and created_channel:
                try:
                    c = await guild.create_text_channel(create_channel_name)
                    notice_channels.append(c)
                except discord.Forbidden:
                    Error_guild.append(f"Error: Guild ({guild.id}), Forbidden!")
        
        for channel in notice_channels:
            try:
                await channel.send(to_send)
            except discord.HTTPException:
                Error_guild.append(f"Error: Guild ({channel.server.id}) Channel ({channel.id}) , HTTPException!")
            except discord.Forbidden:
                Error_guild.append(f"Error: Guild ({channel.server.id}) Channel ({channel.id}) , Forbidden!")
            else:
                success_send.append(channel.server.id)
        
        print({"Success_Send":success_send, "Error_send":Error_guild})

        try:
            return await app.close()
        except:
            return

class DPNKClient(discord.Client):
    def __init__(self, send, token, create_channel=None):
        dpnk_client = DPNKDiscordClient(send, create_channel_names=create_channel)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="모든 프로그래밍 언어를 위한 DPNK Module형!")
    parser.add_argument("String", help="공지할 메시지를 작성해주세요!", type=str)
    parser.add_argument("Token", help="디스코드 봇의 토큰을 입력해주세요!", type=str)

    parser.add_argument("-cc", "--create_channel", help="이 선택 인자를 선택하면 채널이 없을때 선택인자의 텍스트를 채널이름으로 생성후 발송합니다!")
    args = parser.parse_args()

    send_text = args.String
    bot_token = args.Token

    err_create_channel = args.create_channel

    dpnk_client = DPNKDiscordClient(send_text, create_channel_names=err_create_channel)
