from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities


async def lucky_egg_ko_effect(ctx):
    """If the holder is Knocked Out by damage from an opponent's attack, draw until 7 in hand."""
    if not ctx.ko_from_attack:
        return
    await ctx.draw_until(7)


card = PokemonToolCardDef(
    guid="7e0ea976-39b2-524d-b66f-5aa6d809eb51",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyEgg.Name",
    display_name="Lucky Egg",
    searchable_by=["Lucky Egg", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=167,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lucky Egg",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=lucky_egg_ko_effect,
        ),
    ],
)
