"""STUB: effect not implemented — do not guess mechanics.
Xatu (DP3 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="7e7ebf71-dcc7-5c4c-8925-89a9fbd9a8a8",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Psychic Shift",
            game_text="Once during your turn, if Xatu is on your Bench, you may choose 1 Special Condition from 1 of your Active Pok\u00e9mon and remove that Special Condition. Then, 1 of the Defending Pok\u00e9mon is now affected by that Special Condition that you chose.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Energy Singe",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage plus 10 more damage for each Energy attached to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)