"""STUB: effect not implemented — do not guess mechanics.
Groudon ex (EX5 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import ignore_resistance_attack


from spirit.game.card_effects.ex import crushing_mantle, mark_of_antiquity_passive

card = PokemonCardDef(
    guid="2171418c-71c8-51f7-87cb-1f09a3fcd9f0",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "ex", "Groudonex"],
    subtypes=["Basic", "ex"],
    collector_number=93,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Ability(
            title="Mark of Antiquity",
            game_text="As long as Groudon ex is your Active Pok\u00e9mon, each player's Kyogre ex and Rayquaza ex can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=mark_of_antiquity_passive("Kyogre ex", "Rayquaza ex"),
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=ignore_resistance_attack(),
        ),
        Attack(
            title="Crushing Mantle",
            game_text="You may discard from your hand as many Energy cards as you like. If you do, this attack does 50 damage plus 10 more damage for each Energy card you discarded.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=crushing_mantle(10, 10),
        ),
    ],
)