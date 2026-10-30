"""STUB: effect not implemented — do not guess mechanics.
Sharpedo (DP3 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="829cd0e1-5020-553c-8a1f-34cc1df1bf0c",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Sharpedo"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If Sharpedo is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Sharpedo is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Strike Wound",
            game_text="If the Defending Pok\u00e9mon has 2 or more damage counters on it, this attack does 60 damage plus 20 more damage. This attack damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)