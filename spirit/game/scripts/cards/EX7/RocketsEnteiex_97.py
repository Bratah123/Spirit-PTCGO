from spirit.game.card_effects.ex import energy_link_self, volcanic_ash, dark_condition_no_weakness_passive
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Entei ex (EX7 #97): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=dark_condition_no_weakness_passive(),
    guid="024d1c1e-22ad-5830-a8ee-e036af6c8317",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsEnteiex.Name",
    display_name="Rocket's Entei ex",
    searchable_by=["Rocket's Entei ex", "Basic", "ex", "RocketsEnteiex"],
    subtypes=["Basic", "ex"],
    collector_number=97,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Dark Condition",
            game_text="As long as Rocket's Entei ex has any Darkness Energy attached to it, Rocket's Entei ex has no Weakness.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Energy Link",
            game_text="Search your discard pile for an Energy card and attach it to Rocket's Entei ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=energy_link_self(),
        ),
        Attack(
            title="Volcanic Ash",
            game_text="Discard 2 Energy attached to Rocket's Entei ex and then choose 1 of your opponent's Pok\u00e9mon. This attack does 60 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=volcanic_ash(),
        ),
    ],
)