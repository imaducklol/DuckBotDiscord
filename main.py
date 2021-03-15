import discord

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

'''
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith(';; '):
		fmessage = message.content[3:]
		str(fmessage).lower()
		print(fmessage)
		# search catholic.com
		if fmessage.startswith('csearch'):
			fmessage = fmessage[7:]
			for j in googlesearch.search('site:catholic.com:' + fmessage, tld="com", num=1, stop=1, pause=2):
				await message.channel.send(j)
		# get catholic calender stuff
		if fmessage.startswith('daily'):
			fmessage = fmessage[5:]
			response = requests.get('http://calapi.inadiutorium.cz/api/v0/en/calendars/general-en/today')
			data = json.loads(response.text)
			await message.channel.send(
				str(data['weekday']).upper() + '\n' + str(data['celebrations'][0]['rank']) + '\n' + str(
					data['celebrations'][0]['title']))

		# await message.channel.send('Hello!')
'''

