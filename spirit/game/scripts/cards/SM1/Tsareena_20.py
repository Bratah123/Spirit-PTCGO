from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers


async def _floral_gain(ctx):
    """60; heal 20 and remove all Special Conditions from this Pokemon."""
    await ctx.deal_damage()
    await ctx.heal(20, ctx.attacker)
    await ctx.cure_all_conditions(ctx.attacker)


async def _queenly_majesty(ctx):
    """On evolve: you may have your opponent reveal their hand; discard a card from it."""
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    if not await ctx.ask_yes_no("Have your opponent reveal their hand and discard a card from it?"):
        return
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    picks = await ctx.choose_cards(hand, 1, minimum=1, display_cards=hand,
                                   prompt="Choose a card to discard")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="fb3dea45-2a49-5a9f-b3b2-94303853429d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name",
    display_name="Tsareena",
    searchable_by=["Tsareena", "Stage 2", "Tsareena"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    abilities=[
        Ability(
            title="Queenly Majesty",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may have your opponent reveal their hand. Then, discard a card from it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=_queenly_majesty,
        ),
        Attack(
            title="Trop Kick",
            game_text="Heal 20 damage and remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_floral_gain,
        ),
    ],
)