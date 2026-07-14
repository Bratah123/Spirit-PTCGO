from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def discreet_draw(ctx):
    """On evolve: you may draw 2 cards."""
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="3d80cd6a-0006-50ca-b0ab-bf8c218270ac",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    display_name="Golbat",
    searchable_by=["Golbat", "Stage 1", "Golbat"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Discreet Draw",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may draw 2 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=discreet_draw,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)