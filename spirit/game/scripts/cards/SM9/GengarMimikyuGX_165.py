from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card

from spirit.game.card_effects.sm9 import (
    horror_house_gx,
)

async def poltergeist(ctx):
    """Opponent reveals their hand; 50 damage for each Trainer card found there."""
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id)
    count = sum(1 for c in cards if is_trainer_card(c))
    await ctx.deal_damage(50 * count)

card = PokemonCardDef(
    guid="47aceeb0-c98c-54ff-9591-11e475e759c8",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarMimikyuGX.Name",
    display_name="Gengar & Mimikyu-GX",
    searchable_by=["Gengar & Mimikyu-GX", "Basic", "TAG TEAM", "GX", "GengarMimikyuGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=165,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=94,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            damage_operator="x",
            effect=poltergeist,
        ),
        Attack(
            title="Horror House-GX",
            game_text="Your opponent can't play any cards from their hand during their next turn. If this Pok\u00e9mon has at least 1 extra Psychic Energy attached to it (in addition to this attack's cost), each player draws cards until they have 7 cards in their hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=horror_house_gx,
        ),
    ],
)