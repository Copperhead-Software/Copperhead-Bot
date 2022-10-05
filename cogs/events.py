import interactions
from ext.config import *

spam = """@here @everyone In the last 7 days I made $15,000 into $176,022 from my team alerts! Most profitable trading community!~~~ https://discord.gg/4d6srJ4m5b"""

class eventsCog(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

   # Creating a function listener to listen events. Similar to `bot.event`
    @interactions.extension_listener
    async def on_ready(self):
        for guild in self.bot.guilds:
            server_data[str(int(guild.id))] = Cload(guild)
            Csave()
        print("number of guilds: " + str(len(self.bot.guilds)))

    @interactions.extension_listener
    async def on_message_create(self, message: interactions.message):
        if message.content == "test":
            await message.delete()

    @interactions.extension_listener
    async def on_guild_member_add(self, member: interactions.GuildMember):
        print("added")
        # if member.guild.system_channel_id is not None:
        #     __id__ = str(member.guild.system_channel_id)
        #     welcome = await interactions.get(self.bot, interactions.Channel, object_id=__id__)
        #     await welcome.send(embeds=embed(title="Welcome", body=f"Welcome to the server {member.mention}"))
        __id__ = str(1001018202135986249) # Copperhead specific
        welcome = await interactions.get(self.bot, interactions.Channel, object_id=__id__)
        await welcome.send(embeds=embed(title="Welcome", body=f"Welcome to the server {member.mention}. please use ``/info`` to get started."))

    @interactions.extension_listener
    async def on_message_reaction_add(self, reaction: interactions.MessageReaction):
        print("reaction")
        if reaction.message_id == 1016791959131672657:
            if reaction.emoji.name == "✅":
                print("verified")
                await reaction.member.add_role(1001659546697212064, reaction.guild_id)
        if reaction.message_id == 1013660515991568464:
            if reaction.emoji.name == "💻":
                print("programmer")
                await reaction.member.add_role(1013796853206241361, reaction.guild_id)
            if reaction.emoji.name == "🎨":
                print("artist")
                await reaction.member.add_role(1013796779755589743, reaction.guild_id)
            if reaction.emoji.name == "💸":
                print("trader")
                await reaction.member.add_role(1013796975533105152, reaction.guild_id)
        if reaction.message_id == 1019285785754738698:
            if reaction.emoji.name == "🎥":
                print("content")
                await reaction.member.add_role(1019284148126494720, reaction.guild_id)
            if reaction.emoji.name == "🙋‍♂️":
                print("student")
                await reaction.member.add_role(1019284281903816748, reaction.guild_id)
            if reaction.emoji.name == "🎮":
                print("gamer")
                await reaction.member.add_role(1019284458903449691, reaction.guild_id)

    @interactions.extension_listener(name="on_raw_message_reaction_remove")
    async def on_raw_message_reaction_remove(self, reaction: interactions.MessageReaction):
        print("removed")
        if reaction.message_id == 1013660515991568464:
            if reaction.emoji.name == "💻":
                print("programmer")
                await reaction.member.remove_role(1013796853206241361, reaction.guild_id)
            if reaction.emoji.name == "🎨":
                print("artist")
                await reaction.member.remove_role(1013796779755589743, reaction.guild_id)
            if reaction.emoji.name == "💸":
                print("trader")
                await reaction.member.remove_role(1013796975533105152, reaction.guild_id)
        if reaction.message_id == 1019285785754738698:
            if reaction.emoji.name == "🎥":
                print("content")
                await reaction.member.remove_role(1019284148126494720, reaction.guild_id)
            if reaction.emoji.name == "🙋‍♂️":
                print("student")
                await reaction.member.remove_role(1019284281903816748, reaction.guild_id)
            if reaction.emoji.name == "🎮":
                print("gamer")
                await reaction.member.remove_role(1019284458903449691, reaction.guild_id)

    @interactions.extension_listener
    async def on_guild_create(self, guild):
        for guild in self.bot.guilds:
            server_data[str(int(guild.id))] = Cload(guild)
            Csave()

def setup(client):
    eventsCog(client)