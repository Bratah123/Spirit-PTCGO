from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.effects import is_trainer_card


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _electribonus(ctx):
    """Discard a Lightning Energy card from your hand. If you do, draw 3 cards."""
    if not any(_is_lightning_energy(c) for c in ctx.hand()):
        return
    gone = await ctx.discard_from_hand(1, minimum=0, predicate=_is_lightning_energy,
                                       prompt="Discard a Lightning Energy card to draw 3")
    if gone:
        await ctx.draw_cards(3)


async def _poltergeist(ctx):
    """Your opponent reveals their hand; 20 damage times the number of Trainer cards there."""
    hand = await ctx.reveal_hand(ctx.opponent_id)
    await ctx.deal_damage(20 * sum(1 for c in (hand or []) if is_trainer_card(c)))


card = PokemonCardDef(
    guid="45de73f2-b223-5213-99b1-2ad16e4be12d",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Team Plasma", "Rotom"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=49,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Electribonus",
            game_text="Discard a Lightning Energy card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_electribonus,
        ),
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals his or her hand. This attack does 20 damage times the number of Trainer cards in your opponent's hand.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=_poltergeist,
        ),
    ],
)