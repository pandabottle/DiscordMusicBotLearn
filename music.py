import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.command(name='join',help='Type this to bring bot to your vc')
    async def join(self,ctx):
        if ctx.author.voice is None:    #if the person is not in a VC
            await ctx.send("You're not in a VC")
        voice_channel=ctx.author.voice.channel
        if ctx.voice_client is None: #if bot is not in a VC
            await voice_channel.connect()
        
        else:
            await ctx.voice_client.move_to(voice_channel)
    
    @commands.command(name='bye',help='disconnects bot from your vc')
    async def bye(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name='play',help='Plays a song via play <your url here>')
    async def play(self,ctx,url):
        ctx.voice_client.stop() #stops previous song if it was playing it
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        YDL_OPTIONS={'format':'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url,download=False)
            url2=info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)

            vc.play(source)
    
    @commands.command(name='pause',help='pauses the current music')
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("paused ⏸")
    
    @commands.command(name='resume',help='resumes the paused music')
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("paused ⏸")

    @commands.command(name='stop',help='stops the current music. Will require play command to start again')
    async def stop(self,ctx):
        await ctx.voice_client.stop()
        await ctx.send("paused ⏸")

    @commands.command(name='boom',help='vine boom sfx')
    async def boom(self,ctx):
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
    
    @commands.command(name='ded',help='Ded')
    async def ded(self,ctx):
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
    async def hades(self,ctx):
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
    client.add_cog(music(client))