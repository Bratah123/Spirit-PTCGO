"""STUB: effect not implemented — do not guess mechanics.
Machamp BREAK (XY12 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcd50a09-b009-59a5-ae2c-ed5a4072522b",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampBREAK.Name",
    display_name="Machamp BREAK",
    searchable_by=["Machamp BREAK", "BREAK", "MachampBREAK"],
    subtypes=["BREAK"],
    collector_number=60,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Boomerang Lariat",
            game_text="During your next turn, this Pok\u00e9mon's attacks do 100 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)