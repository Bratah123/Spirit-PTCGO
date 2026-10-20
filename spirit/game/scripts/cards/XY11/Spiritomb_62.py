from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import _is_damaged


async def _damage_play(ctx):
    """Move any number of damage counters from the opponent's Benched Pokemon
    to their other Pokemon in any way you like."""
    for _ in range(60):
        pool = [p for p in ctx.opponent_bench() if _is_damaged(ctx.board, p)]
        if not pool:
            return
        src = await ctx.choose_pokemon(pool, "Move damage counters from which Benched Pokémon? (decline to stop)", optional=True)
        if src is None:
            return
        dests = [p for p in ctx.opponent_pokemon_in_play() if p is not src]
        if not dests or not await ctx.move_damage_counters(src, dests):
            return


card = PokemonCardDef(
    guid="2cafdf1c-ea9d-51c6-8fde-c1ca55ef82d0",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title="Nightmare",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Damage Play",
            game_text="Move as many damage counters on your opponent's Benched Pok\u00e9mon as you like to any of your opponent's other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=_damage_play,
        ),
    ],
)