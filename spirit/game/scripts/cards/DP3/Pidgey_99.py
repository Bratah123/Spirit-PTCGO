"""STUB: effect not implemented — do not guess mechanics.
Pidgey (DP3 #99): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import charm_reduce_defender_next


card = PokemonCardDef(
    guid="b47bb843-38ae-5568-b9ac-10a00d3efb2f",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=16,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=charm_reduce_defender_next(20),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)