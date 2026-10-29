from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm10 import (
    red_knuckles,
    resetting_hole,
    resetting_hole_condition,
)

card = PokemonCardDef(
    guid="a904f2ff-10bd-58f9-a800-fd6cfd5e66d2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Marshadow"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=802,
    abilities=[
        Ability(
            title="Resetting Hole",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may discard any Stadium card in play. If you do, discard this Pok\u00e9mon and all cards attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=resetting_hole_condition,
            effect=resetting_hole
        ),
        Attack(
            title="Red Knuckles",
            game_text="If your opponent's Active Pok\u00e9mon is an Ultra Beast, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=red_knuckles
        ),
    ],
)