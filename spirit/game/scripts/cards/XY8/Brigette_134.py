from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_basic_pokemon


def _is_ex(card):
    return "EX" in (getattr(def_for(card.archetype_id), "subtypes", None) or [])


async def brigette(ctx):
    """Search your deck for 1 Basic Pokemon-EX or 3 Basic Pokemon (except
    Pokemon-EX) and put them onto your Bench. Shuffle."""
    pick = await ctx.choose("Brigette", ["1 Basic Pokémon-EX", "3 Basic Pokémon (not EX)"])
    if pick == 0:
        await search_to_bench(lambda c: is_basic_pokemon(c) and _is_ex(c), 1,
                              prompt="Choose a Basic Pokémon-EX")(ctx)
    else:
        await search_to_bench(lambda c: is_basic_pokemon(c) and not _is_ex(c), 3,
                              prompt="Choose up to 3 Basic Pokémon")(ctx)


card = SupporterCardDef(
    guid="562e45e6-0f03-5a12-b9b3-9be90088ecb3",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name",
    display_name="Brigette",
    searchable_by=["Brigette", "Supporter"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=brigette
)
