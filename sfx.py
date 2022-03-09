import discord
from discord.ext import commands
import youtube_dl

class Sfx(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(name='boom',help='vine boom sfx')
    async def boom(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=829pvBHyG6I'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='chilling',help='Zhong Xina')
    async def chilling(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlbc='https://www.youtube.com/watch?v=KH_XIt-hm2Y'
                info = ydl.extract_info(urlbc,download=False)
                urlbic=info['formats'][0]['url']
                sssource = await discord.FFmpegOpusAudio.from_probe(urlbic,**FFMPEG_OPTIONS)

                vc.play(sssource)
        
    @commands.command(name='dog',help='what is it doin?')
    async def dog(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlbc='https://www.youtube.com/watch?v=SdmfidIYS84'
                info = ydl.extract_info(urlbc,download=False)
                urlbic=info['formats'][0]['url']
                sssource = await discord.FFmpegOpusAudio.from_probe(urlbic,**FFMPEG_OPTIONS)

                vc.play(sssource)

    @commands.command(name='sus',help='when the imposter')
    async def sus(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlbc='https://www.youtube.com/watch?v=ekL881PJMjI'
                info = ydl.extract_info(urlbc,download=False)
                urlbic=info['formats'][0]['url']
                sssource = await discord.FFmpegOpusAudio.from_probe(urlbic,**FFMPEG_OPTIONS)

                vc.play(sssource)

    @commands.command(name='fart',help='special fart')
    async def fart(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=Qi1KebO4bzc'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='mad',help='why u haf to be mad')
    async def mad(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=xzpndHtdl9A'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='baby',help='Why are you baby?')
    async def baby(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=j3glwtXrj0c'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)

    @commands.command(name='lag',help='Your internet')
    async def lag(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=E52eC_XoSqI'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='stopit',help='Just stop')
    async def stopit(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=GLRJT5IU88s'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)

    @commands.command(name='bruh',help='bruh')
    async def bruh(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=2ZIpFytCSVc'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='bs',help='What I am hearing from you')
    async def bs(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=-TzHx9ByBCs'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)

    @commands.command(name='throw',help='Flashbang out')
    async def throw(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=X5e2NCWN9ac'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='ded',help='Dark Souls death')
    async def ded(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
            YDL_OPTIONS={'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=j_nV2jcTFvA'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
    
    @commands.command(name='hades',help='Hadeez nuts')
    async def hades(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn -t 5'}
            YDL_OPTIONS={'format':'worstaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=B5leUzYa_qo'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)
        
    @commands.command(name='idol',help='Super idol')
    async def idol(self,ctx):
        voice_channel = ctx.author.voice.channel
        voice = ctx.voice_client

        if (voice_channel is None): #if user not in VC, send message
            await ctx.send("You're not in a VC")
        
        if (voice is None):   #if bot not in vc, join the channel
            await voice_channel.connect()
        
        if (voice is not None and voice.channel is not voice_channel):
            print("aint there. Coming right now")
            await voice.move_to(voice_channel)
            voice = ctx.voice_client  #update the value

        else:   #else it is already there
            ctx.voice_client.stop() #stops previous song if it was playing it
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn -t 13.49'}
            YDL_OPTIONS={'format':'worstaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                """
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                """
                
                urlboom='https://www.youtube.com/watch?v=HvUY80Dhgxo'
                iinfo = ydl.extract_info(urlboom,download=False)
                urlbm=iinfo['formats'][0]['url']
                ssource = await discord.FFmpegOpusAudio.from_probe(urlbm,**FFMPEG_OPTIONS)

                vc.play(ssource)

def setup(client):
    client.add_cog(Sfx(client))