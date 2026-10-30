"""STUB: effect not implemented — do not guess mechanics.
Latios ex δ (EX15 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import ice_barrier_then_damage, link_wing_named_retreat0
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="293cc6c2-2a0a-50fa-8a57-1853ebd5d9d1",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiosex.Name",
    display_name="Latios ex δ",
    searchable_by=["Latios ex \u03b4", "Basic", "ex", "Latiosex"],
    subtypes=["Basic", "ex"],
    collector_number=96,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=381,
    abilities=[
        Ability(
            title="Link Wing",
            game_text="The Retreat Cost for each of your Latias, Latias ex, Latios, and Latios ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=link_wing_named_retreat0("latias", "latios"),
        ),
        Attack(
            title="Ice Barrier",
            game_text="Prevent all effects of attack, including damage, done to Latios ex by your opponent's Pok\u00e9mon-ex during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=ice_barrier_then_damage(),
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)