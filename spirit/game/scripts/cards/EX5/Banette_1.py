"""STUB: effect not implemented — do not guess mechanics.
Banette (EX5 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import darkness_chant, shadow_steal

card = PokemonCardDef(
    guid="53da8a7f-aca5-5a40-b20d-acfcc1a0e851",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Shadow Steal",
            game_text="Does 10 damage plus 20 more damage for each Special Energy card in your opponent's discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=shadow_steal(),
        ),
        Attack(
            title="Darkness Chant",
            game_text="Count the number of Basic Pok\u00e9mon or Evolution cards in your discard pile. Put that many damage counters on the Defending Pok\u00e9mon. You can't put more than 6 damage counters on the Defending Pok\u00e9mon in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=darkness_chant(),
        ),
    ],
)