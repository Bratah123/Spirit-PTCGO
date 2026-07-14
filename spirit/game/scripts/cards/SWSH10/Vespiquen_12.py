from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_sweet_honey(card):
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == "Sweet Honey"


async def honey_rush(ctx):
    """Reveal any number of Sweet Honey cards from your hand. This attack
    does 60 damage for each card revealed this way."""
    honey = [c for c in ctx.hand() if _is_sweet_honey(c)]
    picks = []
    if honey:
        picks = await ctx.choose_cards(
            honey, len(honey), minimum=0,
            prompt="Reveal any number of Sweet Honey cards.",
        )
    if picks:
        await ctx.reveal_cards(picks)
    amount = 60 * len(picks)
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="3f8da2c4-4d4d-5be0-b622-1ada25962532",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Honey Rush",
            game_text="Reveal any number of Sweet Honey cards from your hand. This attack does 60 damage for each card you revealed in this way.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            damage_operator="x",
            effect=honey_rush,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)