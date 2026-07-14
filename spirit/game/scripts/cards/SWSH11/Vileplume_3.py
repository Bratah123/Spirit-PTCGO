from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.session.effects import is_supporter_card, is_item_card


async def allergy_storm(ctx):
    """90. Flip a coin: heads locks Supporters, tails locks Items, next opponent turn."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Allergy Storm"))[0]
    if heads:
        ctx.lock_plays(ctx.opponent_id, is_supporter_card)
    else:
        ctx.lock_plays(ctx.opponent_id, is_item_card)


card = PokemonCardDef(
    guid="139b1799-a247-5785-b7c2-3daa812983f8",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=heal_attack(30),
        ),
        Attack(
            title="Allergy Storm",
            game_text="Flip a coin. If heads, during your opponent's next turn, they can't play any Supporter cards from their hand. If tails, during your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=allergy_storm,
        ),
    ],
)