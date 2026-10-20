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
    guid="26c86b53-ae72-5957-85f8-74f837298c04",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2", "Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=76,
    set_code="BW11",
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
