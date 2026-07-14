from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


async def spill_out(ctx):
    """60+150. Discard your hand. If you discarded 5 or more cards this way, +150 damage."""
    hand = ctx.hand()
    count = len(hand)
    await ctx.discard_cards(hand)
    await ctx.deal_damage(60 + (150 if count >= 5 else 0))


card = PokemonCardDef(
    guid="15fe97d0-39ab-543a-8dd0-71f704425543",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name",
    display_name="Greedent",
    searchable_by=["Greedent", "Stage 1", "Greedent"],
    subtypes=["Stage 1"],
    collector_number=151,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Spill Out",
            game_text="Discard your hand. If you discarded 5 or more cards in this way, this attack does 150 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=spill_out,
        ),
    ],
)