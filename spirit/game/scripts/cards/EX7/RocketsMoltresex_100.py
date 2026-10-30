from spirit.game.card_effects.ex import fire_dance, dark_lift_passive_ex7
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Moltres ex (EX7 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=dark_lift_passive_ex7(),
    guid="fdfc6f21-2dcf-5693-b30d-01f6823366d8",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMoltresex.Name",
    display_name="Rocket's Moltres ex",
    searchable_by=["Rocket's Moltres ex", "Basic", "ex", "RocketsMoltresex"],
    subtypes=["Basic", "ex"],
    collector_number=100,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Dark Lift",
            game_text="If Rocket's Moltres ex has any Darkness Energy attached to it, the Retreat Cost for Rocket's Moltres ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Fire Dance",
            game_text="Search your discard pile for a Fire Energy card and attach it to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=fire_dance(),
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)