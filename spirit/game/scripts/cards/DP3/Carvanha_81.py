"""STUB: effect not implemented — do not guess mechanics.
Carvanha (DP3 #81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0faf626e-42bd-5b31-bbc9-a829ea0e7a7c",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    display_name="Carvanha",
    searchable_by=["Carvanha", "Basic", "Carvanha"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=318,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Bite Away",
            game_text="Flip a coin. If heads, choose a card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)