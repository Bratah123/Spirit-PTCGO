from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per


async def future_sight(ctx):
    """Look at the top 5 cards of your deck and put them back in any order."""
    await ctx.reorder_deck_top(5)


def _is_reuniclus(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    return definition is not None and definition.display_name == "Reuniclus"


card = PokemonCardDef(
    guid="b6f70c8d-3520-56b7-8e8b-377e1e80c99a",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2", "Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=577,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 5 cards of your deck and put them back on top of your deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=future_sight,
        ),
        Attack(
            title="Net Force",
            game_text="Does 40 damage times the number of Reuniclus you have in play.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", pred=_is_reuniclus), 40),
        ),
    ],
)
