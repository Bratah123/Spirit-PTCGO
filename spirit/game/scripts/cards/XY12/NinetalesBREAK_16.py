"""STUB: effect not implemented — do not guess mechanics.
Ninetales BREAK (XY12 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="814beafe-cdef-521d-9272-bfb73b281127",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NinetalesBREAK.Name",
    display_name="Ninetales BREAK",
    searchable_by=["Ninetales BREAK", "BREAK", "NinetalesBREAK"],
    subtypes=["BREAK"],
    collector_number=16,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Explosive Fireball",
            game_text="Discard all Fire Energy attached to this Pok\u00e9mon. This attack does 60 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)