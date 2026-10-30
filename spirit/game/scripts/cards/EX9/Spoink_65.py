"""STUB: effect not implemented — do not guess mechanics.
Spoink (EX9 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="a435ffe2-dc06-5782-8064-9fefe18efe63",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    display_name="Spoink",
    searchable_by=["Spoink", "Basic", "Spoink"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=325,
    abilities=[
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)