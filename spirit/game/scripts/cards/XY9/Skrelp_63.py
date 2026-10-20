"""STUB: effect not implemented — do not guess mechanics.
Skrelp (XY9 #63): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5443b24b-27ba-5397-8196-e9e96d19a8dc",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    display_name="Skrelp",
    searchable_by=["Skrelp", "Basic", "Skrelp"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=690,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)