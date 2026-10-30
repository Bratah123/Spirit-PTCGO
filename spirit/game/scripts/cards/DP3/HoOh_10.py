"""STUB: effect not implemented — do not guess mechanics.
Ho-Oh (DP3 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5c82d7a6-3a02-53f0-8ca4-ae3915057743",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="DP3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title="Phoenix Turn",
            game_text="Once during your opponent's turn, if Ho-Oh would be Knocked Out by damage from an attack, you may flip a coin. If heads, Ho-Oh isn't discarded. Instead, remove all damage counters, Special Conditions, and other effects from Ho-Oh. Then, discard all cards attached to Ho-Oh (except for Energy cards). This counts as Ho-Oh being Knocked Out and your opponent takes a Prize card.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Wing",
            game_text="This attack does 20 damage times the number of different types of basic Energy cards attached to Ho-Oh.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)