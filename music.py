import discord
from discord.ext import commands
import youtube_dl

queues = []

class Music(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(name='play',help='play <your url here>')
    async def play(self,ctx,url):
        #First, we note down the VC the user and bot are in
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
                info = ydl.extract_info(url,download=False)
                url2=info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)

                vc.play(source)
    
    @commands.command(name='bye',help='disconnects bot from your vc')
    async def bye(self,ctx):
        await ctx.voice_client.disconnect()
    
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

def setup(client):
    client.add_cog(Music(client))