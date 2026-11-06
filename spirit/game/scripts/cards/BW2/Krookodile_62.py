from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import in_active_spot


def _black_eyes_condition(board, player_id, pokemon) -> bool:
    if not in_active_spot(board, player_id, pokemon):
        return False
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    active = board.active_pokemon(opponent)
    return active is not None and bool(board.attached_energies(active))


async def black_eyes(ctx):
    """Once/turn if Active: flip; heads discard Energy from opp Active."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not results or not results[0]:
        return
    target = ctx.opponent_active()
    if target is None:
        return
    await ctx.discard_energy_from(
        target, 1,
        prompt="Choose Energy to discard from the Defending Pokémon",
    )


card = PokemonCardDef(
    guid="3da2c124-e0ee-5885-85be-32854b5092ce",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2", "Krookodile"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Ability(
            title="Black Eyes",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_black_eyes_condition,
            effect=black_eyes,
        ),
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 20 more damage. If tails, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=flip_damage(bonus=20, require_all=True, tails_self_damage=20),
        ),
    ],
)
