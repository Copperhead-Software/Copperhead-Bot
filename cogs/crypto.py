import interactions
import requests
from ext.config import *

class crypto(interactions.Extension):
    def __init__(self) -> None:
        super().__init__()
        self.bot: interactions.Client = self.client

    @interactions.extension_command(
        name="price",
        description="Gets the price of a cryptocurrency",
        options=[
            interactions.Option(
                name="coin",
                description="The coin to get the price of",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[
                    interactions.Choice("SOL", "SOL"),
                    interactions.Choice("BTC", "BTC"),
                    interactions.Choice("ETH", "ETH"),
                    interactions.Choice("DOGE", "DOGE"),
                    interactions.Choice("ADA", "ADA"),
                    interactions.Choice("DOT", "DOT"),
                    interactions.Choice("LTC", "LTC"),
                    interactions.Choice("XRP", "XRP"),
                    interactions.Choice("LINK", "LINK"),
                    interactions.Choice("BCH", "BCH"),
                    interactions.Choice("BNB", "BNB"),
                    interactions.Choice("UNI", "UNI"),
                    interactions.Choice("FIL", "FIL"),
                    interactions.Choice("XLM", "XLM"),
                    interactions.Choice("MATIC", "MATIC"),
                    interactions.Choice("THETA", "THETA"),
                    interactions.Choice("VET", "VET"),
                    interactions.Choice("TRX", "TRX"),
                ]
            ),
        ],
    )
    async def price(self, ctx, coin):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
        data = requests.get(url)
        data = data.json()
        print("checked")
        price = data["price"].strip("0")
        await ctx.send(embeds=embed(title=f"{coin} Price", body=f"1 {coin}: ${price} (USD)", footer="Powered by Binance"))

def setup(bot):
    bot.add_extension(crypto())