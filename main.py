"""
Github GNU General Public License version 3.0 (GPLv3)

Copyright 매리 2018, All Right Reserved.
"""

owner = []

import asyncio
import discord 
import setting

set = setting.set()

app = discord.Client()


@app.event
async def on_ready():
    print("Mary Notice Module for" , app.user.name, " (%s)" % app.user.id)
    owner.append(set.owner)

@app.event
async def on_message(message):
    if message.author.id == app.user.id: return

    if set.log:
        print("Channel: %s(%s) | Author: %s(#%s) | Message: %s" % (
            message.channel, str(message.channel.id)[:5],
            message.author.name, str(message.author.id),
            message.content
	    	))

    s = set.first + set.no
    if s in message.content:
        if message.author.id in owner:
            notice = message.content.replace(s, "")
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신 준비중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_footer(text="DPNK - StayCute")
            mssg = await message.channel.send(embed=embed)
            a = []
            b = []
            e = []
            ec = {}
            embed=discord.Embed(title="공지 시스템", color=0x80ff80)
            embed.add_field(name="공지 발신중!", value="<@" + message.author.id + ">", inline=True)
            embed.set_footer(text="DPNK - StayCute")
            await mssg.edit(embed=embed)
            for server in app.guilds:
                for channel in server.channels:
                    for tag in set.allowprefix:
                        if tag in channel.name:
                            dtat = True
                            for distag in set.disallowprefix:
                                if distag in channel.name:
                                    dtat = False
                            if dtat:
                                if not server.id in a:
                                    try:
                                        await channel.send(notice)
                                    except discord.HTTPException:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "HTTPException"
                                    except discord.Forbidden:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "Forbidden"
                                    except discord.NotFound:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "NotFound"
                                    except discord.InvalidArgument:
                                        e.append(str(channel.id))
                                        ec[channel.id] = "InvalidArgument"
                                    else:
                                        a.append(str(server.id))
                                        b.append(str(channel.id))
            asdf = "```\n"
            for server in app.servers:
                if not server.id in a:
                    if set.nfct:
                        try:
                            ch = await server.create_text_channel(set.nfctname)
                            await ch.send(notice)
                        except:
                            asdf = asdf + str(server.name) + "[채널 생성 실패]\n"
                        else:
                            asdf = asdf + str(server.name) + "[채널 생성 및 재발송 성공]\n"
                    else:
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
                es = es + str(app.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
            bs = bs + "```"
            es = es + "```"
            if bs == "``````":
                bs = "``` ```"
            if es == "``````":
                es = "``` ```"
            if asdf == "``````":
                asdf = "``` ```"
            sucess = bs
            missing = es
            notfound = asdf
            embed.add_field(name="공지 발신 성공 채널:", value=sucess, inline=True)
            embed.add_field(name="공지 발신 실패 채널:", value=missing, inline=True)
            embed.add_field(name="공지 채널 없는 서버:", value=notfound, inline=True)
            embed.set_footer(text="DPNK - StayCute")
            await mssg.edit(embed=embed)
        else:
            await message.channel.send("봇 제작자만 사용할수 있는 커맨드입니다!")


app.run(set.token)
