"""STUB: effect not implemented — do not guess mechanics.
Shiftry (EX5 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import push_aside, supernatural_power

card = PokemonCardDef(
    guid="a801094b-d180-5eb5-a04d-d1a0019dae19",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Push Aside",
            game_text="Look at your opponent's hand and choose 1 Basic Pok\u00e9mon or Evolution card you find there. Your opponent puts it at the bottom of his or her deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=push_aside(),
        ),
        Attack(
            title="Supernatural Power",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 40 damage plus 40 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=supernatural_power(40, 40),
        ),
    ],
)