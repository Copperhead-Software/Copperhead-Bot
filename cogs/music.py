from interactions.ext.voice import VoiceState
import interactions
from pytube import YouTube
from asyncio import sleep

class music(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    @interactions.extension_listener
    async def on_voice_state_update(vs: VoiceState):
        print(vs.self_mute)
    
    @interactions.extension_command(name="connect", description="connect to your voice channel", options=[
        interactions.Option("channel", "the channel you want to connect to", interactions.OptionType.CHANNEL, required=True)
    ])
    async def connect(self, ctx, channel):
        await self.bot.connect_vc(channel_id=int(channel.id), guild_id=int(ctx.guild_id), self_deaf=True, self_mute=False)
        await ctx.send("Connected to your voice channel")

    @interactions.extention_command(name="play", description="play a song from youtube", options=[
        interactions.Option("link", "the link of the song you want to play", interactions.OptionType.STRING, required=True)
    ])
    async def play(self, ctx, link):
        name = YouTube(link).title
        self.queue.append(name)
        for song in self.queue:
            await self.bot.play(file=f"mp3/{song}.mp3")
            message = await ctx.send(f"now playing {song}...")
            sleep(5)
            await message.delete()

    @interactions.extension_command(name="pause", description="pause the current song")
    async def pause(self, ctx):
        await self.bot.pause()
        await ctx.send("paused the current song")

    @interactions.extension_command(name="resume", description="resume the current song")
    async def resume(self, ctx):
        await self.bot.resume()
        await ctx.send("resumed the current song")
    
    @interactions.extension_command(name="stop", description="stop the current song")
    async def stop(self, ctx):
        await self.bot.stop()
        await ctx.send("stopped the current song")

    @interactions.extension_command(name="disconnect", description="disconnects from your voice channel")
    async def disconnect(self, ctx):
        await self.bot.disconnect_vc()
        await ctx.send("disconnected from your voice channel")

def setup(bot):
    bot.add_extension(music(bot))