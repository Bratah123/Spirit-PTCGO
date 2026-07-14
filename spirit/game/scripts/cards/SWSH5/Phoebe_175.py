from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_pokemon_vmax, has_vmax_in_play


async def phoebe(ctx):
    """This turn, your Pokemon VMAX's attack damage ignores effects on the opponent's Active."""
    for pokemon in ctx.my_pokemon_in_play():
        if is_pokemon_vmax(pokemon.archetype_id):
            ctx.ignore_own_target_effects(pokemon)


card = SupporterCardDef(
    guid="1dd665c8-7c4f-593d-aa28-9afe91e0f052",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Phoebe.Name",
    display_name="Phoebe",
    searchable_by=["Phoebe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SWSH5",
    rarity=Rarities.RareRainbow,
    effect=phoebe,
    condition=has_vmax_in_play
)
