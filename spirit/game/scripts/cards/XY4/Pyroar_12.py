from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _flare_condition(board, player_id, pokemon=None):
    opp = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opp, "bench") if opp else None
    return (pokemon is not None and any(_is_fire_energy(c) for c in pokemon.children)
            and bool(bench and bench.children))


async def _flare_command(ctx):
    """Discard a Fire Energy from this Pokemon: switch 1 of your opponent's
    Benched Pokemon with their Active Pokemon."""
    discarded = await ctx.discard_energy_from(ctx.source, 1, predicate=_is_fire_energy,
                                              minimum=1, prompt="Discard a Fire Energy")
    bench = ctx.opponent_bench()
    if not discarded or not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    await ctx.switch_active(ctx.opponent_id, target or bench[0])


card = PokemonCardDef(
    guid="86b62ae9-c659-50e2-bd90-bb27f643b63b",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Ability(
            title="Flare Command",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy attached to this Pok\u00e9mon. If you do, switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flare_condition,
            effect=_flare_command,
        ),
        Attack(
            title="Inferno Onrush",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=recoil_attack(30),
        ),
    ],
)