"""STUB: effect not implemented — do not guess mechanics.
M Sceptile-EX (XY7 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait

card = PokemonCardDef(
    guid="078d89f2-1516-55b6-b58f-b08a3f9153d5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSceptileEX.Name",
    display_name="M Sceptile-EX",
    searchable_by=["M Sceptile-EX", "MEGA", "EX", "MSceptileEX"],
    subtypes=["MEGA", "EX"],
    collector_number=8,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SceptileEX.Name",
    family_id=254,
    abilities=[
        ancient_trait('θ Stop'),
        Attack(
            title="Jagged Saber",
            game_text="You may attach up to 2 Grass Energy cards from your hand to your Benched Pok\u00e9mon in any way you like. If you attached Energy to a Pok\u00e9mon in this way, heal all damage from that Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)