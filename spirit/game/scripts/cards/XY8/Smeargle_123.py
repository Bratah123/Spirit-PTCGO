from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _coat_condition(board, player_id, pokemon=None):
    a = board.active_pokemon(player_id)
    discard = board.find_player_area(player_id, "discard")
    return a is not None and any(is_basic_energy_card(c) for c in a.children) \
        and bool(discard) and any(is_basic_energy_card(c) for c in discard.children)


async def _second_coat(ctx):
    """Switch a basic Energy attached to your Active with a different type of basic Energy from your discard."""
    a = ctx.my_active()
    attached = [e for e in ctx.attached_energies(a) if is_basic_energy_card(e)] if a else []
    if not attached:
        return
    old = await ctx.choose_cards(attached, 1, minimum=1, prompt="Choose a basic Energy to switch")
    if not old:
        return
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c) and c.archetype_id != old[0].archetype_id]
    if not pool:
        return
    new = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a different basic Energy")
    if new:
        await ctx.discard_cards(old)
        await ctx.attach_energy(new[0], a)


card = PokemonCardDef(
    guid="4b59e871-d207-577e-b5ba-2b8d9dec1794",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic", "Smeargle"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Ability(
            title="Second Coat",
            game_text="Once during your turn (before your attack), you may switch a basic Energy card attached to your Active Pok\u00e9mon with a different type of basic Energy card from your discard pile.",
            activation=Activations.ONCE_PER_TURN,
            condition=_coat_condition,
            effect=_second_coat,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)