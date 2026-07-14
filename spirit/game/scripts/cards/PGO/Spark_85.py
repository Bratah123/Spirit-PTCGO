from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_lightning_energy_card(card):
    if not is_basic_energy_card(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.LIGHTNING.value in types


async def _spark(ctx):
    drawn = await ctx.draw_cards(2)
    if drawn <= 0:
        return
    heads = (await ctx.flip_coins(1, "Spark"))[0]
    if not heads:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    energies = [c for c in ctx.discard_pile() if _is_lightning_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Lightning Energy card from your discard pile.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="9cf50c38-d3d9-557b-8911-1c349f0ead04",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Spark.Name",
    display_name="Spark",
    searchable_by=["Spark", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="PGO",
    rarity=Rarities.RareRainbow,
    effect=_spark,
)
