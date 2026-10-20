from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _connect_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    return board.active_pokemon(player_id) is not None and bool(bench) and any(
        is_basic_energy_card(c) for p in bench.children for c in p.children)


async def _energy_connect(ctx):
    """Move a basic Energy from 1 of your Benched Pokemon to your Active Pokemon."""
    sources = [p for p in ctx.my_bench() if any(is_basic_energy_card(e) for e in ctx.attached_energies(p))]
    active = ctx.my_active()
    if sources and active is not None:
        await ctx.move_energy_freely(sources, [active], predicate=is_basic_energy_card, max_count=1,
                                     prompt="Choose a basic Energy to move")


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _electricannon(ctx):
    """80; you may discard all Lightning Energy from this Pokemon for 50 more damage."""
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _is_lightning_energy(e)]
    if pool and await ctx.ask_yes_no("Discard all Lightning Energy for 50 more damage?"):
        await ctx.discard_cards(pool)
        await ctx.deal_damage(130)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="6d39d43a-79ab-5b26-bdbb-7fca309e8ec8",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Eelektross"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Ability(
            title="Energy Connect",
            game_text="As often as you like during your turn (before your attack), you may move a basic Energy attached to 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_connect_condition,
            effect=_energy_connect,
        ),
        Attack(
            title="Electricannon",
            game_text="You may discard all Lightning Energy attached to this Pok\u00e9mon. If you do, this attack does 50 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=_electricannon,
        ),
    ],
)