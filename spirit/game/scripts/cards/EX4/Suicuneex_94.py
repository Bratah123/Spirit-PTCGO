"""STUB: effect not implemented — do not guess mechanics.
Suicune ex (EX4 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import energy_flip, reverse_stream

card = PokemonCardDef(
    guid="7d06b7e3-4950-527d-9806-4ba3c37348be",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicuneex.Name",
    display_name="Suicune ex",
    searchable_by=["Suicune ex", "Basic", "ex", "Suicuneex"],
    subtypes=["Basic", "ex"],
    collector_number=94,
    set_code="EX4",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Energy Flip",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. You may move an Energy card attached to that Pok\u00e9mon to another of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=energy_flip(),
        ),
        Attack(
            title="Reverse Stream",
            game_text="You may return all basic Energy cards attached to Suicune ex to your hand. If you do, this attack does 50 damage plus 10 more damage for each basic Energy card you returned.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=reverse_stream(),
        ),
    ],
)