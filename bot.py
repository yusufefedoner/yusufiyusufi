import discord
from discord.ext import commands
from logic import get_city_coordinates, get_all_cities, create_graph

TOKEN = "BURAYA_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


VALID_COLORS = [
    "red", "blue", "green", "yellow",
    "purple", "black", "orange", "pink"
]


@bot.command()
async def city(ctx, color, *, city_name):
    if color.lower() not in VALID_COLORS:
        await ctx.send(f"Geçersiz renk. Kullanılabilir renkler: {', '.join(VALID_COLORS)}")
        return

    coords = get_city_coordinates(city_name)

    if not coords:
        await ctx.send("Şehir bulunamadı.")
        return

    lat, lon = coords
    file_name = create_graph(
        [(city_name, lat, lon)],
        marker_color=color.lower()
    )

    await ctx.send(file=discord.File(file_name))


@bot.command()
async def allcities(ctx, color="red"):
    if color.lower() not in VALID_COLORS:
        await ctx.send(f"Geçersiz renk. Kullanılabilir renkler: {', '.join(VALID_COLORS)}")
        return

    cities = get_all_cities()

    if not cities:
        await ctx.send("Veritabanında şehir yok.")
        return

    file_name = create_graph(
        cities,
        marker_color=color.lower()
    )

    await ctx.send(file=discord.File(file_name))


bot.run(TOKEN)
