from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, AttrID


async def _sitrus_berry(ctx):
    pokemon = ctx.source
    counters = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
    if counters < 3:
        return
    await ctx.heal(30, target=pokemon)
    tool = next((t for t, p in ctx.tools_in_play() if p is pokemon), None)
    if tool is not None:
        await ctx.discard_cards([tool])


card = PokemonToolCardDef(
    guid="87854b57-1540-5037-b0e6-9cd44286a79c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SitrusBerry.Name",
    display_name="Sitrus Berry",
    searchable_by=["Sitrus Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Sitrus Berry",
            game_text="At the end of each turn, if the Pok\u00e9mon this card is attached to has 3 or more damage counters on it, heal 30 damage from it and discard this card.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=_sitrus_berry,
        ),
    ],
)
