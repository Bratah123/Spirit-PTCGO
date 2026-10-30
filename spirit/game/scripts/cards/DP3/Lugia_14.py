"""STUB: effect not implemented — do not guess mechanics.
Lugia (DP3 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b2558fe8-1e49-5903-b01c-1ad81057f683",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title="Silver Wing",
            game_text="Flip a coin. If heads, choose an Energy card attached to the Defending Pok\u00e9mon and return it to your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Destruction",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, this attack's base damage is 40 instead of 120.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)