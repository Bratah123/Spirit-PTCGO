from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken


def _from_basic(calc, carrier):
    return calc.target is carrier_pokemon(carrier) and calc.attacker is not None and is_basic_pokemon(calc.attacker)


async def _quick_guard(ctx):
    """Prevent all damage done to this Pokemon by attacks from Basic Pokemon during the opponent's next turn."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, prevent_damage_when(_from_basic))


card = PokemonCardDef(
    guid="84d6522b-651b-5a8a-99ad-1eade3614bb2",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic", "Cobalion"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Attack(
            title="Quick Guard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon during your opponent's next turn. This Pok\u00e9mon can't use Quick Guard during your next turn.",
            cost={PokemonTypes.METAL: 1},
            effect=_quick_guard,
            locks_next_turn=True,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.METAL: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), 30, base=30),
        ),
    ],
)