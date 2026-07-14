from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining


async def fickle_impact(ctx):
    """180. Does nothing if you have exactly 2, 4, or 6 Prize cards remaining."""
    if count_prizes_remaining("mine")(ctx) in (2, 4, 6):
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="94ddfcca-a01b-52d2-bd80-5db0c2500c03",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Fickle Impact",
            game_text="If you have exactly 2, 4, or 6 Prize cards remaining, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=fickle_impact,
        ),
    ],
)