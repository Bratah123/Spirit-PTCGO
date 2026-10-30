"""STUB: effect not implemented — do not guess mechanics.
Togepi δ (EX15 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import charm_reduce_defender_next
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7abd6bbe-e8ac-5d16-8798-57b51c329c03",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi δ",
    searchable_by=["Togepi \u03b4", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=175,
    abilities=[
        Attack(
            title="Charm",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=charm_reduce_defender_next(20),
        ),
    ],
)