"""STUB: effect not implemented — do not guess mechanics.
Poliwrath (XY12 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="beaa41bd-f8a1-5325-9618-1d638cdf4d4b",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Dashing Punch",
            game_text="If this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, this attack does 50 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Whirlpool",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)