import discord
from discord.ext import commands

class Covid19(commands.cog): 
    def __init__(self, bot):
        self.bot=bot

    @commands.command(name='Covid19')
    async def Covid19(self, ctx, city):
        if city == "군산":
            pass
        elif city == "서울":
            pass
        else:
            ctx.send("찾을 수 없는 지역입니다.") 
    
        embed=discord.Embed(title="Covid19", description=f'{date} 오늘의 확진자 수입니다.', color=0x29428b)
        embed.add_field(
            name='군산',
            value='\n'.join(Gunsan)
        )
        embed.add_field(
            name='서울',
            value='\n'.join(Seoul)
        )
        embed.add_field(
            name='한국',
            value='\n'.join(Korea)
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Covid19(bot)) 
