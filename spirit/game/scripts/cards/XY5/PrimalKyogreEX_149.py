"""STUB: effect not implemented — do not guess mechanics.
Primal Kyogre-EX (XY5 #149): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait

card = PokemonCardDef(
    guid="0402dd4a-3edc-539a-90d8-d42e42a3ac82",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimalKyogreEX.Name",
    display_name="Primal Kyogre-EX",
    searchable_by=["Primal Kyogre-EX", "MEGA", "EX", "PrimalKyogreEX"],
    subtypes=["MEGA", "EX"],
    collector_number=149,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name",
    family_id=382,
    abilities=[
        ancient_trait('α Growth'),
        Attack(
            title="Tidal Storm",
            game_text="Move 2 Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. This attack does 30 damage to each of your opponent's Benched Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)