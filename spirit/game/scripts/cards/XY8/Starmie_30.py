from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw


async def _balance_bind(ctx):
    """30; if both players have the same number of Benched Pokemon, Paralyze."""
    await ctx.deal_damage()
    if len(ctx.my_bench()) == len(ctx.opponent_bench()):
        await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="8265df0b-0693-5bc4-a300-934599ca8931",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Deep Sea Swirl",
            game_text="Shuffle your hand into your deck. Then, draw 7 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=shuffle_hand_into_deck_draw(7),
        ),
        Attack(
            title="Balance Bind",
            game_text="If you and your opponent have the same number of Benched Pok\u00e9mon, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_balance_bind,
        ),
    ],
)