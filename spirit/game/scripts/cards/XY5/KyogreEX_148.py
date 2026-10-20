"""STUB: effect not implemented — do not guess mechanics.
Kyogre-EX (XY5 #148): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="7312fe38-4d85-55c8-9f0b-edd961944f86",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name",
    display_name="Kyogre-EX",
    searchable_by=["Kyogre-EX", "Basic", "EX", "KyogreEX"],
    subtypes=["Basic", "EX"],
    collector_number=148,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Giant Whirlpool",
            game_text="Return 2 Water Energy attached to this Pok\u00e9mon to your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)