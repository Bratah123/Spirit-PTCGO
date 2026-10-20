from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def _circuit_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_energy_card(c) and _is_lightning_energy(c) for c in hand.children)


async def _magnetic_circuit(ctx):
    """Attach a Lightning Energy card from your hand to 1 of your Pokemon."""
    pool = [c for c in ctx.hand() if is_energy_card(c) and _is_lightning_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Lightning Energy card")
    mine = ctx.my_pokemon_in_play()
    target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach to which Pokémon?")
    if picks and target is not None:
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="d1c753de-5dea-5afe-a995-ba08ebcdca4c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Magnetic Circuit",
            game_text="As often as you like during your turn (before your attack), you may attach a Lightning Energy card from your hand to 1 of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_circuit_condition,
            effect=_magnetic_circuit,
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard a Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.LIGHTNING),
        ),
    ],
)