from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import TurnDamageModifier


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _steam_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and any(_is_fire_energy(c) for c in hand.children))


def _basic_fire(p):
    return is_basic_pokemon(p) and PokemonTypes.FIRE.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _steam_up(ctx):
    """Discard a Fire Energy card from your hand: this turn your Basic Fire
    Pokemon's attacks do 30 more to the opponent's Active (before W/R)."""
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=_is_fire_energy,
                                         prompt="Discard a Fire Energy card")
    if picked:
        ctx.add_turn_damage_modifier(TurnDamageModifier(30, ctx.player_id, source_predicate=_basic_fire))


card = PokemonCardDef(
    guid="7594e1de-ff5c-5c0d-8948-8a92ca6d2b87",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionEX.Name",
    display_name="Volcanion-EX",
    searchable_by=["Volcanion-EX", "Basic", "EX", "VolcanionEX"],
    subtypes=["Basic", "EX"],
    collector_number=115,
    set_code="XY11",
    rarity=Rarities.RareSecret,
    hp=180,
    elements=[PokemonTypes.FIRE, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Steam Up",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, during this turn, your Basic Fire Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            activation=Activations.ONCE_PER_TURN,
            condition=_steam_condition,
            effect=_steam_up,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_freeze_shock,
        ),
    ],
)