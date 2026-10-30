"""STUB: effect not implemented — do not guess mechanics.
Latias ex δ (EX15 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import fellow_boost_attach_energy, power_crush_discard_on_ko
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="bb0c94fa-00fe-5a0b-8b9d-6ea8bd4aac81",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiasex.Name",
    display_name="Latias ex δ",
    searchable_by=["Latias ex \u03b4", "Basic", "ex", "Latiasex"],
    subtypes=["Basic", "ex"],
    collector_number=95,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Ability(
            title="Fellow Boost",
            game_text="Once during your turn (before your attack), you may attach a basic Energy card from your hand to your Latias, Latias ex, Latios, or Latios ex. If you do, your turn ends. This power can't be used if Latias ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=fellow_boost_attach_energy("latias", "latios"),
        ),
        Attack(
            title="Power Crush",
            game_text="If the Defending Pok\u00e9mon is Knocked Out by this attack, discard 2 Fire Energy attached to Latias ex.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=power_crush_discard_on_ko(),
        ),
    ],
)