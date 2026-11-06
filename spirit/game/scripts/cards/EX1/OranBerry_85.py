from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import AttrID, Rarities

_ORAN_BERRY_GUID = "6a4b0b44-0dd5-571e-9423-3a6f1f4e37d4"


async def oran_berry_checkup(ctx):
    """Between turns: if the holder has at least 2 damage counters, heal 20
    and discard this card."""
    pokemon = ctx.source
    counters = (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
    if counters < 2:
        return
    await ctx.heal(20, target=pokemon)
    tool = next((c for c in pokemon.children if c.archetype_id == _ORAN_BERRY_GUID), None)
    if tool is not None:
        await ctx.discard_cards([tool])


card = PokemonToolCardDef(
    guid="6a4b0b44-0dd5-571e-9423-3a6f1f4e37d4",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OranBerry.Name",
    display_name="Oran Berry",
    searchable_by=["Oran Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=85,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Oran Berry",
            game_text="At any time between turns, if the Pok\u00e9mon this card is attached to has at least 2 damage counters on it, remove 2 damage counters from it. Then discard Oran Berry.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=oran_berry_checkup,
        ),
    ],
)
