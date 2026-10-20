from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.session.passives import carrier_pokemon


async def frost_wall(ctx):
    """30. During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Evolution Pokemon."""
    await ctx.deal_damage()
    passive = prevent_damage_when(
        lambda calc, carrier: carrier_pokemon(carrier) is calc.target
        and is_evolution_pokemon(calc.attacker)
    )
    ctx.add_passive_through_opponents_turn(ctx.attacker, passive)


card = PokemonCardDef(
    guid="d1de258b-0622-53e4-9137-d5cda537ba31",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonEX.Name",
    display_name="Glaceon-EX",
    searchable_by=["Glaceon-EX", "Basic", "EX", "GlaceonEX"],
    subtypes=["Basic", "EX"],
    collector_number=20,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=471,
    abilities=[
        Attack(
            title="Second Bite",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on('defender'), 10, base=20),
        ),
        Attack(
            title="Crystal Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=frost_wall,
        ),
    ],
)