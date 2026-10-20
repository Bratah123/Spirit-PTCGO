"""STUB: effect not implemented — do not guess mechanics.
Huntail (XY5 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9bdee64b-2343-5fd1-add4-ea84387ce574",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1", "Huntail"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Attack(
            title="Powerful Storm",
            game_text="This attack does 20 damage times the amount of Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)