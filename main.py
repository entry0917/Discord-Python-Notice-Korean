owner = []

"""
설정 부분입니다.
"""

#공지할 사람의 ID 입력
owner.append("공지할 사람의 ID 입력")
#봇의 토큰 입력
token = "토큰 입력"

#봇의 접두사 입력
first = "!"

#봇의 공지 명령어 입력
no = "공지"

"""
이밑에 부터는 건들면 뒤짐!!!!

Github MIT Lisence.

Copyright 매리 2018, All Right Reserved.
"""

import asyncio
import discord  # 디스코드 모듈
import requests

client = discord.Client()

app = discord.Client()  # 챗봇 지정

bot_deleting = True

maker = "351613953769603073"

# --- 이벤트영역 ---
@app.event
async def on_ready():
    print("Mary Notice Module for" , app.user.name, " (%s)" % app.user.id)
    #매리의 ID 건들면 뒤짐
    owner.append("351613953769603073")
# 메세지
@app.event
async def on_message(message):
    if message.author.id == app.user.id: return

    print("Channel: %s(%s) | Author: %s(#%s) | Message: %s" % (
        message.channel, message.channel.id[:5],
        message.author.name, message.author.id,
        message.content
		))
    s = first + no
    if s in message.content:
        if message.author.id in owner:
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신 준비중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="by 매리(#4633)", icon_url="https://cdn.discordapp.com/avatars/351613953769603073/b4805197b14b4366c3aaebaf79109fa8.webp")
            embed.set_footer(text="Notice Module by Mary")
            mssg = await app.send_message(message.channel, embed=embed)
            notice = message.content.replace(s, "")
            a = []
            b = []
            e = []
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_author(name="by 매리(#4633)", icon_url="https://cdn.discordapp.com/avatars/351613953769603073/b4805197b14b4366c3aaebaf79109fa8.webp")
            embed.set_footer(text="Notice Module by Mary")
            await app.edit_message(mssg, embed=embed)
            for server in app.servers:
                for channel in server.channels:
                    if 'notice' in channel.name:
                        if not 'ban' in channel.name:
                            if not 'worry' in channel.name:
                                if not 'punish' in channel.name:
                                    if not 'guild' in channel.name:
                                        if not server.id in a:
                                            try:
                                                id = channel.id
                                                msg = app.get_channel(id)
                                                await app.send_message(msg, notice)
                                            except:
                                                e.append(str(channel.id))
                                            else:
                                                a.append(str(server.id))
                                                b.append(str(channel.id))
            for server in app.servers:
                for channel in server.channels:
                    if '공지' in channel.name:
                        if not '밴' in channel.name:
                            if not '경고' in channel.name:
                                if not '제재' in channel.name:
                                    if not '길드' in channel.name:
                                        if not server.id in a:
                                            try:
                                                id = channel.id
                                                msg = app.get_channel(id)
                                                await app.send_message(msg, notice)
                                            except:
                                                e.append(str(channel.id))
                                            else:
                                                a.append(str(server.id))
                                                b.append(str(channel.id))
            asdf = "```\n"
            for server in app.servers:
                if not server.id in a:
                    asdf = asdf + str(server.name) + "\n"
            asdf = asdf + "```"
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신완료!", value="<@" + message.author.id + ">", inline=True)
            bs = "```\n"
            es = "```\n"
            for bf in b:
                bn = app.get_channel(bf).name
                bs = bs + str(bn) + "\n"
            for ef in e:
                en = app.get_channel(ef).name
                es = es + str(en) + "\n"
            bs = bs + "```"
            es = es + "```"
            if bs == "``````":
                bs = "``` ```"
            if es == "``````":
                es = "``` ```"
            if asdf == "``````":
                asdf = "``` ```"
            embed.add_field(name="공지 발신 성공 채널:", value=bs, inline=True)
            embed.add_field(name="공지 발신 실패 채널:", value=es, inline=True)
            embed.add_field(name="공지 채널 없는 서버:", value=asdf, inline=True)
            embed.set_author(name="by 매리(#4633)", icon_url="https://cdn.discordapp.com/avatars/351613953769603073/b4805197b14b4366c3aaebaf79109fa8.webp")
            embed.set_footer(text="Notice Module by Mary")
            await app.edit_message(mssg, embed=embed)
        else:
            await app.send_message(message.channel, "봇 제작자만 사용할수 있는 커맨드입니다!")

# 봇 실행
app.run(token)