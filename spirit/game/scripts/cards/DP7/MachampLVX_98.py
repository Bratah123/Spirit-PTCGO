"""STUB: effect not implemented — do not guess mechanics.
Machamp LV.X (DP7 #98): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a7f76bab-a749-5313-8619-a0a907d88d46",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampLVX.Name",
    display_name="Machamp LV.X",
    searchable_by=["Machamp LV.X", "Level-Up", "MachampLVX"],
    subtypes=["Level-Up"],
    collector_number=98,
    set_code="DP7",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.LEVELUP,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    family_id=66,
    abilities=[
        Ability(
            title="No Guard",
            game_text="As long as Machamp is your Active Pok\u00e9mon, each of Machamp's attacks does 60 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance) and any damage done to Machamp by your opponent's Pok\u00e9mon is increased by 60 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Strong-Willed",
            game_text="During your opponent's next turn, if Machamp would be Knocked Out by damage from an attack, flip a coin. If heads, Machamp is not Knocked Out and its remaining HP becomes 10 instead.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)