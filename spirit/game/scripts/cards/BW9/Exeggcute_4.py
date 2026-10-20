from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def _propagation(ctx):
    """Once during your turn, if this Pokemon is in your discard pile, you may
    put it into your hand."""
    await ctx.put_in_hand([ctx.source], reveal=True)


card = PokemonCardDef(
    guid="5539136b-dc3d-5c73-a2b5-a7ca95f8b8e7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic", "Exeggcute"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=102,
    abilities=[
        Ability(
            title="Propagation",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put this Pok\u00e9mon into your hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            effect=_propagation,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)