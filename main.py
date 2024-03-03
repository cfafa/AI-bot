from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os, random
import requests
import discord
from discord.ext import commands





name_class = path

def getclass_detect(path):
  np.set_printoptions(suppress=True)
  model = load_model("keras_model.h5", compile=False)
  class_names = open("labels.txt", "r").readlines()
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open(path).convert("RGB")

  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  image_array = np.asarray(image)

  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1


  data[0] = normalized_image_array

  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]


  return class_name[2:-1]



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    for attachment in ctx.message.attachments:
        name = attachment.filename
        link = attachment.url
        await attachment.save(f'images/{name}')
        await ctx.send('Картинка сохранена')
    else:
        await ctx.send('вы не загрузили картинку')


bot.run('TOKEN')
