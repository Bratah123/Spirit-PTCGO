"""STUB: effect not implemented — do not guess mechanics.
Zangoose (EX9 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.card_effects.ex import bonus_if_ex
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="bd118867-7679-5ae3-9185-a3a19d0e3ed6",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic", "Zangoose"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Extra Claws",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if_ex(20),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(10),
        ),
    ],
)