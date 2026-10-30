"""STUB: effect not implemented — do not guess mechanics.
Duskull (DP3 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98bbc77f-f8c5-5b47-9fd0-c1a3e49db080",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=355,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose 1 card from your opponent's hand without looking. Look at that card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)