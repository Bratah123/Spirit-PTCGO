"""STUB: effect not implemented — do not guess mechanics.
Raichu BREAK (XY8 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="94b94ac0-b095-5087-a542-885731fc1cc5",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuBREAK.Name",
    display_name="Raichu BREAK",
    searchable_by=["Raichu BREAK", "BREAK", "RaichuBREAK"],
    subtypes=["BREAK"],
    collector_number=50,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Grand Bolt",
            game_text="Discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)