"""STUB: effect not implemented — do not guess mechanics.
Bidoof (XY5 #116): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a72fd754-7704-5c23-9df2-7ceee70f72e5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    display_name="Bidoof",
    searchable_by=["Bidoof", "Basic", "Bidoof"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=399,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Scrunch",
            game_text="Flip a coin. If heads, prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)