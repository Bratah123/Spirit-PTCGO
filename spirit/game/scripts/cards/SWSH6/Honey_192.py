from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.data_utils import is_pokemon_v


async def honey(ctx):
    """Draw a card for each of your opponent's Benched Pokemon V."""
    count = sum(1 for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id))
    if count:
        await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="f05d29cd-fd6f-597b-9830-1da1ef089e1d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Honey.Name",
    display_name="Honey",
    searchable_by=["Honey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    effect=honey,
)
