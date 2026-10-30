from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import _is_damaged


async def _transfer_pain(ctx):
    """Move 1 damage counter from 1 of your Pokemon to 1 of your opponent's Pokemon."""
    pool = [p for p in ctx.my_pokemon_in_play() if _is_damaged(ctx.board, p)]
    if not pool:
        return
    src = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Move a damage counter from which Pokémon?")
    if src is not None:
        await ctx.move_damage_counters(src, ctx.opponent_pokemon_in_play(), max_count=1)


card = PokemonCardDef(
    guid="0b3c5bae-b743-5170-9a44-c21cce55d3f4",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=425,
    abilities=[
        Attack(
            title="Transfer Pain",
            game_text="Move 1 damage counter from 1 of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_transfer_pain,
        ),
    ],
)