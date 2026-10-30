from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.sm3 import rock_wrecker


async def mountain_roasting(ctx):
    """On evolve: you may discard the top 3 cards of your opponent's deck."""
    if await ctx.ask_yes_no("Discard the top 3 cards of your opponent's deck?"):
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="c86e11f5-7abb-5541-93c1-542d44f39371",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Ability(
            title="Toppling Wind",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard the top 3 cards of your opponent's deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            # STUB: ability effect not implemented
            trigger=Triggers.ON_EVOLVE,
            effect=mountain_roasting,
        ),
        Attack(
            title="Rock Wrecker",
            game_text="This attack's damage isn't affected by Weakness or Resistance. This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=rock_wrecker,
        ),
    ],
)
