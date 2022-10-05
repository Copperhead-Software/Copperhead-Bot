import interactions
from ext.config import *

class tools(interactions.Extension):
    def __init__(self, client):
        self.bot: interactions.Client = client

    @interactions.extension_command(name="info")
    async def info(self, ctx: interactions.CommandContext):
        await ctx.send(embeds=embed(title="Copperhead", body="Welcome to the server! heres some info to get you started. \n\nif you're looking to have something made for you, please open a ticket in <#1013657456385200208>. \n\nif you want to talk about NFTs, Crypto, or just are here for the community, go to <#1001018202135986249> and hang out! also make sure to check out <#1011886916016296017>"))

    @interactions.extension_command(
        name="job",
        description="post your job listing!",
    )
    async def job(self, ctx):
        new = interactions.Button(
            style=interactions.ButtonStyle.PRIMARY,
            label="new posting",
            custom_id="new"
        )
        update = interactions.Button(
            style=interactions.ButtonStyle.PRIMARY,
            label="update posting",
            custom_id="update"
        )
        boost = interactions.Button(
            style=interactions.ButtonStyle.PRIMARY,
            label="boost post",
            custom_id="boost"
        )
        await ctx.send(embeds=embed("job posting", body="what would you like to do?", color=0x00ff00), components=[new, update, boost], ephemeral=True)

    @interactions.extension_component("new")
    async def new(self, ctx):
        if os.path.exists("jobs/"):
            pass
        else:
            os.mkdir("jobs")
        if os.path.exists(f"jobs/{ctx.author}.txt"):
            await ctx.send("you already have a job listing! use /boost to boost your listing", ephemeral=True)
            return
        modal = interactions.Modal(
            title="Job Listing",
            custom_id="job",
            components=[
                interactions.TextInput(
                    label="body",
                    placeholder="enter your job listing here",
                    custom_id="body",
                    style=interactions.TextStyleType.PARAGRAPH
                ),
                interactions.TextInput(
                    label="skills",
                    placeholder="enter your skills here",
                    custom_id="skills",
                    style=interactions.TextStyleType.PARAGRAPH
                ),
                interactions.TextInput(
                    label="footer",
                    placeholder="enter your footer here",
                    custom_id="footer",
                    style=interactions.TextStyleType.SHORT
                )
            ]
        )
        await ctx.popup(modal)

    @interactions.extension_modal("job")
    async def modal_response(self, ctx, body, skills, footer):
        body = f"""
{ctx.author}'s job listing:

{body}

{ctx.author}'s skills:
{skills}

{footer}
        """
        with open(f"jobs/{ctx.author}.txt", "w") as f:
            f.write(body)
        await ctx.send("your job listing has been posted", ephemeral=True)

    @interactions.extension_component("update")
    async def update(self, ctx):
        if not os.path.exists(f"jobs/{ctx.author}.txt"):
            await ctx.send("you don't have a job listing! use /job to create one", ephemeral=True)
            return

    @interactions.extension_component("boost")
    async def boost(self, ctx):
        if not os.path.exists(f"jobs/{ctx.author}.txt"):
            await ctx.send("you don't have a job listing! use /job to create one", ephemeral=True)
            return

def setup(client):
  tools(client)
