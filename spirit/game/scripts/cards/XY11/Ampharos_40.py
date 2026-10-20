from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import _other_player


async def _nyan_press(ctx):
    """40+; heads 40 more; tails the opponent's Active is Paralyzed."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    heads = bool(results and results[0])
    await ctx.deal_damage(ctx.ability.damage + (40 if heads else 0))
    if not heads:
        await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


def _shocking_condition(board, player_id, pokemon=None):
    return any(_is_ex(p) for p in board.pokemon_in_play(_other_player(board, player_id)))


async def _shocking_light(ctx):
    """Put 3 damage counters on 1 of your opponent's Pokemon-EX."""
    pool = [p for p in ctx.opponent_pokemon_in_play() if _is_ex(p)]
    if not pool:
        return
    t = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Put 3 damage counters on which Pokémon-EX?")
    if t is not None:
        await ctx.place_damage_counters(3, [t])


card = PokemonCardDef(
    guid="9eb384a6-56b5-5338-ad4a-ae64f6dac685",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=40,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Shocking Light",
            game_text="Once during your turn (before your attack), you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon-EX.",
            activation=Activations.ONCE_PER_TURN,
            condition=_shocking_condition,
            effect=_shocking_light,
        ),
        Attack(
            title="Gigavolt",
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=_nyan_press,
        ),
    ],
)