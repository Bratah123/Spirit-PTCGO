"""STUB: effect not implemented — do not guess mechanics.
Torterra LV.X (DPP #DP09): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2ce4624b-85a7-5531-b0ae-63c4d03aa33b",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TorterraLVX.Name",
    display_name="Torterra LV.X",
    searchable_by=["Torterra LV.X", "Level-Up", "TorterraLVX"],
    subtypes=["Level-Up"],
    collector_number=9,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.LEVELUP,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name",
    family_id=389,
    abilities=[
        Ability(
            title="Forest Murmurs",
            game_text="Once during your turn (before your attack), if you have more Prize cards left than your opponent, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. This power can't be used if Torterra is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Vigorous Dash",
            game_text="Does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Torterra does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)