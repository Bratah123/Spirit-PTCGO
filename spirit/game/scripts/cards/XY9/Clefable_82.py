from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.trainers import is_dragon_pokemon


async def _moon_barrier(ctx):
    """30; during the opponent's next turn, prevent all damage from Dragon Pokemon's attacks to this Pokemon."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, prevent_damage_when(
        lambda calc, carrier: calc.attacker is not None and is_dragon_pokemon(calc.attacker)))


card = PokemonCardDef(
    guid="7fd85dd0-629f-5500-b932-adc5fca48e60",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Moon Barrier",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Dragon Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=_moon_barrier,
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)