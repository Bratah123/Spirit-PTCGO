from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.pokemon import delayed_knockout


async def _doom_desire(ctx):
    """Discard all Energy attached to this Pokemon; the Defending Pokemon is
    Knocked Out at the end of your opponent's next turn."""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies:
        await ctx.discard_cards(energies)
    await delayed_knockout(ctx)


card = PokemonCardDef(
    guid="b76e43f3-e67b-5c13-accc-66ea2d0839a3",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="Diminutive Desire",
            game_text="Look at the top 7 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=look_at_top(7, take=1, rest='shuffle'),
        ),
        Attack(
            title="Doom Desire",
            game_text="Discard all Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon is Knocked Out at the end of your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=_doom_desire,
        ),
    ],
)