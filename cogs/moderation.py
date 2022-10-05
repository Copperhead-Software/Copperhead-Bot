import interactions
from ext.config import *
import asyncio

class mod(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(
        name="clear",
        description="Clears a certain amount of messages",
        default_member_permissions=interactions.Permissions.MANAGE_MESSAGES,
        options=[
            interactions.Option(
                name="amount",
                description="The amount of messages to delete",
                type=interactions.OptionType.INTEGER,
                required=True
            ),
        ]
    )
    async def clear(self, ctx, amount: int):
        def check_pinned(message):
            return not message.pinned
        await ctx.get_guild()
        await ctx.channel.purge(amount, check=check_pinned)
        await ctx.send(embeds=embed(title="Cleared", body=f"{amount} messages have been deleted"), ephemeral=True)

    @interactions.extension_command(
        name="warn",
        description="Warns a user",
        default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to warn",
                type=interactions.OptionType.USER,
                required=True
            ),
            interactions.Option(
                name="reason",
                description="The reason for the warning",
                type=interactions.OptionType.STRING,
                required=True
            )
        ]
    )
    async def warn(self, ctx, user, reason: None):
        if reason is None:
            reason = "No reason given"
        if not os.path.exists(f"guilds/{ctx.guild}"):
            os.mkdir(f"guilds/{ctx.guild}")
        with open(f"guilds/{ctx.guild}/{user}.txt", "a+") as f:
            f.write(reason+"\n")
            # f.close()
        with open(f"guilds/{ctx.guild}/{user}.txt", "r") as f:
            lines = f.readlines()
            if len(lines) >= 4:
                await ctx.send("this is user's 3rd warning. they have been kicked.")
                await user.kick(reason="warned 3 times")
            else:
                print(len(lines))
            # f.close()
        await ctx.send(embeds=embed("Warn", body=f"{user} has been warned for {reason}"))

    @interactions.extension_command(
        name="infractions",
        description="Shows the infractions of a user",
        default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to show the infractions of",
                type=interactions.OptionType.USER,
                required=True
            ),
        ],
    )
    async def infractions(self, ctx, user):
        if not os.path.exists(f"guilds/"):
            os.mkdir(f"guilds/")
        if not os.path.exists(f"guilds/{ctx.guild}"):
            os.mkdir(f"guilds/{ctx.guild}")
        if os.path.exists(f"guilds/{ctx.guild}/{user}.txt"):
            with open(f"guilds/{ctx.guild}/{user}.txt", "r") as f:
                if len(f.readlines()) == -1:
                    await ctx.send(embeds=embed("Infractions", body=f"{user} has no infractions"))
                    return
                else:
                    await ctx.send(f.read())
                    # print(f.read()) 
        else:
            return

    @interactions.extension_command(
        name="kick",
        description="Kicks a user from the server",
        default_member_permissions=interactions.Permissions.KICK_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to kick",
                type=interactions.OptionType.USER,
                required=True
            )
        ]
    )
    async def kick(self, ctx, user, reason: str = None):
        """Kicks a user from the server"""
        await ctx.get_guild()
        await user.kick(guild_id=int(ctx.guild_id), reason=reason)
        await ctx.send(embeds=embed(title="Kicked", body=f"{user.mention} has been kicked for {reason}"))

    @interactions.extension_command(
        name="tempban",
        description="Temporarily bans a user from the server",
        default_member_permissions=interactions.Permissions.BAN_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to ban",
                type=interactions.OptionType.USER,
                required=True
            ),
            interactions.Option(
                name="duration",
                description="The duration of the ban",
                type=interactions.OptionType.INTEGER,
                required=True
            ),
            interactions.Option(
                name="reason",
                description="The reason for the ban",
                type=interactions.OptionType.STRING,
                required=False
            )
        ]
    )
    async def tempban(self, ctx, user:interactions.User, duration: int, reason: str = None):
        await ctx.get_guild()
        await user.ban(guild_id=int(ctx.guild_id), reason=reason)
        await ctx.send(embeds=embed(title="Tempbanned", body=f"{user.mention} has been banned for {duration} seconds for {reason}"))
        await asyncio.sleep(duration)
        await user.remove_ban(guild_id=int(ctx.guild_id))

    @interactions.extension_command(
        name="ban",
        description="Bans a user from the server",
        default_member_permissions=interactions.Permissions.BAN_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to ban",
                type=interactions.OptionType.USER,
                required=True
            ),
            interactions.Option(
                name="reason",
                description="The reason for the ban",
                type=interactions.OptionType.STRING,
                required=False
            )
        ]
    )
    async def ban(self, ctx, user:interactions.User, reason: str = None):
        await ctx.get_guild()
        await user.ban(guild_id=int(ctx.guild_id), reason=reason)
        await ctx.send(embeds=embed(title="Banned", body=f"{user.mention} has been banned for {reason}"))

    @interactions.extension_command(
        name="mute",
        description="Mutes a user in the server",
        default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to mute",
                type=interactions.OptionType.USER,
                required=True
            )
        ]
    )
    async def mute(self, ctx, user):
        """allows mods to mute a user"""
        await ctx.get_guild()
        userIn = user
        roleID = int(1013796927810306190)
        await user.add_role(roleID, ctx.guild.id)
        await ctx.send(f"Muted {userIn}") 
        return

    @interactions.extension_command(
        name="unmute",
        description="unmutes a user in the server",
        default_member_permissions=interactions.Permissions.MODERATE_MEMBERS,
        options=[
            interactions.Option(
                name="user",
                description="The user to mute",
                type=interactions.OptionType.USER,
                required=True
            )
        ]
    )
    async def unmute(self, ctx, user):
        """allows mods to mute a user"""
        await ctx.get_guild()
        userIn = user
        roleID = int(1013796927810306190)
        await user.remove_role(roleID, ctx.guild.id)
        await ctx.send(f"Muted {userIn}") 
        return

def setup(client):
    mod(client)