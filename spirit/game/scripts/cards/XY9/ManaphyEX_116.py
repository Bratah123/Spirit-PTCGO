from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def sugary_sprinkles(ctx):
    """Heal 30 damage from each of your Benched Pokemon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _has_water(pokemon, carrier):
    return pokemon.owning_player_id == carrier.owning_player_id and \
        any(is_energy_card(c) and _is_water_energy(c) for c in pokemon.children)


card = PokemonCardDef(
    guid="f50b42b6-18f1-57b1-a439-654d0ec62f41",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManaphyEX.Name",
    display_name="Manaphy-EX",
    searchable_by=["Manaphy-EX", "Basic", "EX", "ManaphyEX"],
    subtypes=["Basic", "EX"],
    collector_number=116,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Ability(
            title="Aqua Tube",
            game_text="Each of your Pok\u00e9mon that has any Water Energy attached to it has no Retreat Cost.",
            passive=retreat_free_when(_has_water),
        ),
        Attack(
            title="Mineral Pump",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=sugary_sprinkles,
        ),
    ],
)