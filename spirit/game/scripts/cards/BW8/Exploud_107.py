from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, has_attack_titled


async def _destructive_sound(ctx):
    """Your opponent reveals their hand. Discard all Item cards you find there."""
    hand = await ctx.reveal_hand(ctx.opponent_id) or []
    items = [c for c in hand if is_item_card(c)]
    if items:
        await ctx.discard_cards(items)


card = PokemonCardDef(
    guid="4b051e86-b75e-56fe-a5a5-025197121682",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=107,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Destructive Sound",
            game_text="Your opponent reveals his or her hand. Discard all Item cards you find there.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_destructive_sound,
        ),
        Attack(
            title="Round",
            game_text="Does 50 damage times the number of your Pok\u00e9mon that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_in_play('mine', has_attack_titled('Round')), 50),
        ),
    ],
)