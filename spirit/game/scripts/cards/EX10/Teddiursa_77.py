"""STUB: effect not implemented — do not guess mechanics.
Teddiursa (EX10 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import teary_eyes_reduce

card = PokemonCardDef(
    guid="3b0c152d-9d8c-549b-a83a-a6198bfac755",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    display_name="Teddiursa",
    searchable_by=["Teddiursa", "Basic", "Teddiursa"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="EX10",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=216,
    abilities=[
        Attack(
            title="Teary Eyes",
            game_text="During your opponent's next turn, any damage done to Teddiursa by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=teary_eyes_reduce(20),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)