"""STUB: effect not implemented — do not guess mechanics.
Kecleon (DP3 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f2ea9c7c-02ab-5ae9-967e-bfd28918eaba",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Kecleon"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Camouflage",
            game_text="If any basic Energy card attached to Kecleon is the same as the Attacking Pok\u00e9mon's type, any damage done by attacks from the Pok\u00e9mon to Kecleon is reduced by 40 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blind Scratch",
            game_text="Flip a coin. If tails, this attack does no damage to the Defending Pok\u00e9mon. Instead, this attack does 20 damage to 1 of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)