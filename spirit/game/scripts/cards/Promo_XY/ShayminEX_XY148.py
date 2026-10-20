from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import _is_damaged
from spirit.game.session.effects import is_basic_pokemon


def _aroma_targets(board, player_id):
    area = board.find_player_area(player_id, "bench")
    return [p for p in (area.children if area else [])
            if is_basic_pokemon(p) and _is_damaged(board, p)]


def _aroma_condition(board, player_id, pokemon):
    return bool(_aroma_targets(board, player_id))


async def _aroma_of_gratitude(ctx):
    """Once during your turn: heal 20 from each of your Benched Basic Pokemon."""
    for p in [p for p in ctx.my_bench() if is_basic_pokemon(p)]:
        await ctx.heal(20, p)


async def _floral_gain(ctx):
    """60; heal 20 and remove all Special Conditions from this Pokemon."""
    await ctx.deal_damage()
    await ctx.heal(20, ctx.attacker)
    await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="db7627e5-ae1d-538b-9867-899fae093bdb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name",
    display_name="Shaymin-EX",
    searchable_by=["Shaymin-EX", "Basic", "EX", "ShayminEX"],
    subtypes=["Basic", "EX"],
    collector_number=148,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Ability(
            title="Aroma of Gratitude",
            game_text="Once during your turn (before your attack), you may heal 20 damage from each of your Benched Basic Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_aroma_condition,
            effect=_aroma_of_gratitude,
        ),
        Attack(
            title="Floral Gain",
            game_text="Heal 20 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_floral_gain,
        ),
    ],
)