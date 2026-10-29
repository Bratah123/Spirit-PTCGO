from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

async def synchrodraw(ctx):
    """Shuffle your hand into your deck. Then, draw a card for each card in
    your opponent's hand."""
    draw_count = ctx.hand_size(ctx.opponent_id)
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(draw_count)

card = PokemonCardDef(
    guid="54cf8247-7691-5ee7-97dc-1ee0d101db83",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chatot.Name",
    display_name="Chatot",
    searchable_by=["Chatot", "Basic", "Chatot"],
    subtypes=["Basic"],
    collector_number=162,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=441,
    abilities=[
        Attack(
            title="Mimic",
            game_text="Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=synchrodraw,
        ),
        Attack(
            title="Tone-Deaf",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)