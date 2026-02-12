import discord
from discord.ext import commands
from logic import get_city_coordinates, get_all_cities, create_graph

TOKEN = "BURAYA_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def city(ctx, *, city_name):
    coords = get_city_coordinates(city_name)

    if not coords:
        await ctx.send("Şehir bulunamadı.")
        return

    lat, lon = coords
    file_name = create_graph([(city_name, lat, lon)])

    await ctx.send(file=discord.File(file_name))


@bot.command()
async def allcities(ctx):
    cities = get_all_cities()

    if not cities:
        await ctx.send("Veritabanında şehir yok.")
        return

    file_name = create_graph(cities)

    await ctx.send(file=discord.File(file_name))


bot.run(TOKEN)
