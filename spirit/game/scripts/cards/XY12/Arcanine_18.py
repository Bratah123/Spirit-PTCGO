from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _burning_road_condition(board, player_id, pokemon=None):
    ts = getattr(board, "turn_state", None)
    if pokemon is None or ts is None or board.active_pokemon(player_id) is not pokemon:
        return False
    if ts.became_active_turn.get(pokemon.entity_id) != ts.turn_number:
        return False
    return any(_is_fire_energy(e) for p in board.pokemon_in_play(player_id) if p is not pokemon
               for e in board.attached_energies(p))


async def _burning_road(ctx):
    """Move any number of Fire Energy attached to your Pokemon to this Pokemon."""
    sources = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    await ctx.move_energy_freely(sources, [ctx.source], predicate=_is_fire_energy,
                                 prompt="Move Fire Energy to this Pokémon")


card = PokemonCardDef(
    guid="8de205ce-7f69-5193-abb9-4747b4aed584",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Burning Road",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, you may move any number of Fire Energy attached to your Pok\u00e9mon to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_burning_road_condition,
            effect=_burning_road,
        ),
        Attack(
            title="Scorching Breath",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=_freeze_shock,
        ),
    ],
)