from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import effective_max_hp
from spirit.game.card_effects.attacks_common import damage_counters_on


def _damaged_others(board, player_id, me):
    return [p for p in board.pokemon_in_play(player_id) if p is not me
            and effective_max_hp(board, p) > p.get_attribute(AttrID.HP, 0)]


def _shadow_void_condition(board, player_id, pokemon=None):
    return pokemon is not None and bool(_damaged_others(board, player_id, pokemon))


async def _shadow_void(ctx):
    """Move 1 damage counter from 1 of your Pokemon to this Pokemon."""
    sources = _damaged_others(ctx.board, ctx.player_id, ctx.source)
    if not sources:
        return
    src = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
        sources, "Move a damage counter from which Pokémon?")
    await ctx.move_damage_counters(src or sources[0], ctx.source, max_count=1)


async def _pain_pellets(ctx):
    """Put damage counters on 1 of your opponent's Pokemon equal to the
    number of damage counters on this Pokemon."""
    n = damage_counters_on('self')(ctx)
    targets = ctx.opponent_pokemon_in_play()
    if n <= 0 or not targets:
        return
    target = await ctx.choose_pokemon(targets, "Put damage counters on which Pokémon?")
    await ctx.deal_damage(n * 10, target=target or targets[0], apply_modifiers=False,
                          as_counters=True)


card = PokemonCardDef(
    guid="0d98eb2a-073f-59e0-85ce-e14f5a1842d7",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=40,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Shadow Void",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to this Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_shadow_void_condition,
            effect=_shadow_void,
        ),
        Attack(
            title="Pain Pellets",
            game_text="Put damage counters on 1 of your opponent's Pok\u00e9mon equal to the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=_pain_pellets,
        ),
    ],
)