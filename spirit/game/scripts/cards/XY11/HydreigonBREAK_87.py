"""STUB: effect not implemented — do not guess mechanics.
Hydreigon BREAK (XY11 #87): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15ecb78f-c21f-5bdb-8584-994878895fea",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HydreigonBREAK.Name",
    display_name="Hydreigon BREAK",
    searchable_by=["Hydreigon BREAK", "BREAK", "HydreigonBREAK"],
    subtypes=["BREAK"],
    collector_number=87,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Calamity Blast",
            game_text="Discard 3 Energy attached to this Pok\u00e9mon. This attack does 50 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)