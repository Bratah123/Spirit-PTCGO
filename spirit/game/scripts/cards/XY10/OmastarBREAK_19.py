"""STUB: effect not implemented — do not guess mechanics.
Omastar BREAK (XY10 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1f6e027-6fc0-53d3-baa7-28bc29f5ca4f",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OmastarBREAK.Name",
    display_name="Omastar BREAK",
    searchable_by=["Omastar BREAK", "BREAK", "OmastarBREAK"],
    subtypes=["BREAK"],
    collector_number=19,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Dangerous Tentacle",
            game_text="Once during your turn (before your attack), you may switch 1 of your opponent's Benched Pok\u00e9mon-EX with his or her Active Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
    ],
)