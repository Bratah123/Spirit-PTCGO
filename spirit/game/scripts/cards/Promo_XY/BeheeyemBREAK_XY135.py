"""STUB: effect not implemented — do not guess mechanics.
Beheeyem BREAK (Promo_XY #XY135): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cd637f2-1e79-5c0c-8a22-54d6c7e4b1c7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BeheeyemBREAK.Name",
    display_name="Beheeyem BREAK",
    searchable_by=["Beheeyem BREAK", "BREAK", "BeheeyemBREAK"],
    subtypes=["BREAK"],
    collector_number=135,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    family_id=606,
    abilities=[
        Attack(
            title="Cosmic Circle",
            game_text="Move as many Psychic Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)