"""STUB: effect not implemented — do not guess mechanics.
Shuckle (DP3 #109): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="82a05704-ec5e-56d5-939d-f20ec83a4693",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Ability(
            title="Pot Shell",
            game_text="Prevent all effects of attacks, including damage, done to Shuckle by your opponent's Pok\u00e9mon that has any Special Energy cards attached to it.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ferment Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned. As long as the Defending Pok\u00e9mon remains Poisoned by this attack, it can't use any Pok\u00e9-Body.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)