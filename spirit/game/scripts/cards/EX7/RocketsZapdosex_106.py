from spirit.game.card_effects.ex import plasma_attach_ex7, raging_thunder_self, darkness_guard_passive
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Zapdos ex (EX7 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=darkness_guard_passive(),
    guid="e32b90b0-2121-5d6f-a047-1d4cec3f4dc1",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsZapdosex.Name",
    display_name="Rocket's Zapdos ex",
    searchable_by=["Rocket's Zapdos ex", "Basic", "ex", "RocketsZapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=106,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=145,
    abilities=[
        Ability(
            title="Darkness Guard",
            game_text="As long as Rocket's Zapdos ex has any Darkness Energy attached to it, damage done to Rocket's Zapdos ex by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Plasma",
            game_text="Search your discard pile for a Lightning Energy card and attach it to Rocket's Zapdos ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=plasma_attach_ex7(),
        ),
        Attack(
            title="Raging Thunder",
            game_text="This attack does 30 damage to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=raging_thunder_self(),
        ),
    ],
)