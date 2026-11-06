from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _hurricane(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        await ctx.move_energy_freely(
            [ctx.attacker], bench, predicate=is_basic_energy_card, max_count=1,
            prompt="Choose a basic Energy to move to a Benched Pokémon",
        )


def _fire_or_fighting(card):
    return is_energy_card(card) and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY) and (
        energy_provides_type(card, PokemonTypes.FIRE.value) or energy_provides_type(card, PokemonTypes.FIGHTING.value))


def _burning_draft_condition(board, player_id, pokemon=None):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard and any(_fire_or_fighting(c) for c in discard.children))


async def _burning_draft(ctx):
    """Attach a Fighting or Fire Energy card from your discard pile to this Pokemon."""
    pool = [c for c in ctx.discard_pile() if _fire_or_fighting(c)]
    if pool:
        pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to attach")
        if pick:
            await ctx.attach_energy(pick[0], ctx.source)


card = PokemonCardDef(
    guid="2a196ea2-1d25-5a3a-a9a5-d18bc8146e2d",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasCamerupt.Name",
    display_name="Team Magma's Camerupt",
    searchable_by=["Team Magma's Camerupt", "Stage 1", "TeamMagmasCamerupt"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Burning Draft",
            game_text="Once during your turn (before your attack), you may attach a Fighting or Fire Energy card from your discard pile to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_burning_draft_condition,
            effect=_burning_draft,
        ),
        Attack(
            title="Flame Ball",
            game_text="Move a basic Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_hurricane,
        ),
    ],
)