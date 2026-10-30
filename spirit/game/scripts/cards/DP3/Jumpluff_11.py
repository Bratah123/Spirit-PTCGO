"""STUB: effect not implemented — do not guess mechanics.
Jumpluff (DP3 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d41654c3-3d6d-5ffe-b043-893c906669ae",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2", "Jumpluff"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Cotton Spore",
            game_text="Whenever Jumpluff would be damaged by your opponent's attack, flip a coin. If heads, prevent all damage done to Jumpluff by that attack.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cottonweed Punch",
            game_text="Flip 2 coins. Choose 1 of your opponent's Pok\u00e9mon. For each heads, this attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)