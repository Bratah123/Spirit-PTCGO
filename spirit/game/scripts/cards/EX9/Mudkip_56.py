"""STUB: effect not implemented — do not guess mechanics.
Mudkip (EX9 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="d6009710-ac89-5f87-a5fa-2a9b58fbaadf",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    display_name="Mudkip",
    searchable_by=["Mudkip", "Basic", "Mudkip"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="EX9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=258,
    abilities=[
        Attack(
            title="Tail Strike",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)