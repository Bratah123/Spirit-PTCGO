from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import AttrID, Rarities

_LUM_BERRY_GUID = "fea6a9ac-0258-56e1-8696-2186eb91ea09"


async def lum_berry_checkup(ctx):
    """End of each turn: if the holder has any Special Condition, cure them
    all and discard this card."""
    pokemon = ctx.source
    if not (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        return
    await ctx.cure_all_conditions(pokemon)
    tool = next((c for c in pokemon.children if c.archetype_id == _LUM_BERRY_GUID), None)
    if tool is not None:
        await ctx.discard_cards([tool])


card = PokemonToolCardDef(
    guid="fea6a9ac-0258-56e1-8696-2186eb91ea09",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumBerry.Name",
    display_name="Lum Berry",
    searchable_by=["Lum Berry", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=168,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lum Berry",
            trigger=Triggers.BETWEEN_TURNS,
            effect=lum_berry_checkup,
        ),
    ],
)
