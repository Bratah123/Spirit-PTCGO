from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.attacks_common import recoil_attack


async def fang_snipe(ctx):
    """30 damage. Opponent reveals their hand; discard a Trainer card found there."""
    await ctx.deal_damage()
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    matches = [c for c in hand if is_trainer_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, minimum=1,
        prompt="Choose a Trainer card to discard from your opponent's hand.",
        display_cards=hand,
    )
    await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="e30c41b3-6c58-5e1e-b340-934e28f2a518",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Fang Snipe",
            game_text="Your opponent reveals his or her hand. Discard a Trainer card you find there.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=fang_snipe,
        ),
        Attack(
            title="Wild Charge",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)