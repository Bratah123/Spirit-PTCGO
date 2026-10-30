"""STUB: effect not implemented — do not guess mechanics.
Scizor (DP7 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ccca89b1-323a-5735-8273-9857ad47bc76",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Honeycomb Defender",
            game_text="If Scizor has 6 or more damage counters on it, any damage done to Scizor by attacks is reduced by 40 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Accelerate",
            game_text="If the Defending Pok\u00e9mon is Knocked Out by this attack, prevent all effects of an attack, including damage, done to Scizor during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pound Down",
            game_text="If you don't have any Pok\u00e9mon with any Pok\u00e9-Powers in play, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)