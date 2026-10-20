"""STUB: effect not implemented — do not guess mechanics.
Talonflame BREAK (XY11 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="078d4ad4-5dd0-5174-87b0-7a6be0b234b8",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TalonflameBREAK.Name",
    display_name="Talonflame BREAK",
    searchable_by=["Talonflame BREAK", "BREAK", "TalonflameBREAK"],
    subtypes=["BREAK"],
    collector_number=21,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)