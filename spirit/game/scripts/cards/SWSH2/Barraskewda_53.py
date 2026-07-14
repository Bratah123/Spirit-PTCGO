from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER)


async def spiral_jet(ctx):
    """Discard 2 Water Energy cards from hand. If you don't, this attack does nothing."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=_is_water_energy_card,
        prompt="Discard 2 Water Energy cards from your hand for Spiral Jet",
    )
    if len(discarded) < 2:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="b5aa2e29-b89c-5cd4-8765-a4e71b923d01",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1", "Barraskewda"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Spiral Jet",
            game_text="Discard 2 Water Energy cards from your hand. If you don't, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=130,
            effect=spiral_jet,
        ),
    ],
)
