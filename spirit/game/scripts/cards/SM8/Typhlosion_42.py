from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    blazing_energy,
    lost_flame,
)

card = PokemonCardDef(
    guid="3dbc7194-93eb-57b3-9f01-b1fd414f1356",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=42,
    set_code="SM8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Blazing Energy",
            game_text="Once during your turn (before your attack), you may use this Ability. All Energy attached to your Pok\u00e9mon are Fire Energy instead of their usual type until the end of your turn. (This includes cards that come into play on this turn.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=blazing_energy,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Lost Flame",
            game_text="Put 2 Energy attached to your opponent's Active Pok\u00e9mon in the Lost Zone.",
            cost={PokemonTypes.FIRE: 4},
            damage=120,
            effect=lost_flame
        ),
    ],
)