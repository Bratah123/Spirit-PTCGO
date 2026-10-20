from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import in_active_spot
import random


async def _lamentation(ctx):
    """If Active and damaged by an opponent's attack (even if KO'd), discard a
    random card from the opponent's hand."""
    pokemon = ctx.source
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    if not in_active_spot(ctx.board, ctx.player_id, pokemon):
        return
    hand = ctx.hand(ctx.opponent_id)
    if hand:
        await ctx.discard_cards([random.choice(hand)])


card = PokemonCardDef(
    guid="e8d12c69-2707-5aaf-b4ef-afc5248d9575",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=178,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Ability(
            title="Lamentation",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), discard a random card from your opponent's hand.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_lamentation,
        ),
        Attack(
            title="Shadow Cage",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)