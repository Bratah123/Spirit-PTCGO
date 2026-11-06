from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


async def _defog(ctx):
    """You may discard any Stadium in play; if you do, +40 damage."""
    bonus = 0
    if ctx.stadium_in_play() is not None and await ctx.ask_yes_no("Discard the Stadium in play for 40 more damage?"):
        if await ctx.discard_stadium() is not None:
            bonus = 40
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="6039f9e4-5d42-55b0-9700-229ab337c1b1",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna", "Stage 1", "Swanna"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    family_id=580,
    abilities=[
        Attack(
            title="Aerial Ace",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Defog",
            game_text="You may discard any Stadium card in play. If you do, this attack does 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_defog,
        ),
    ],
)