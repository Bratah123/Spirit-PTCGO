"""STUB: effect not implemented — do not guess mechanics.
Gligar δ (EX15 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import sting_turn_paralyze_switch, tail_sting_vs_ex
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b854a55-6a3d-5a19-8448-c7cbbe077d44",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar δ",
    searchable_by=["Gligar \u03b4", "Basic", "Gligar"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=207,
    abilities=[
        Attack(
            title="Sting Turn",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and switch Gligar with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=sting_turn_paralyze_switch(),
        ),
        Attack(
            title="Tail Sting",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 10 damage plus 10 more damage and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=tail_sting_vs_ex(10, 10),
        ),
    ],
)