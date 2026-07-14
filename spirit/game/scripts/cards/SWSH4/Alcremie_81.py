from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def sharing_sweets(ctx):
    """On evolve: you may have each player draw a card."""
    if await ctx.ask_yes_no("Have each player draw a card?"):
        await ctx.draw_cards(1)
        await ctx.draw_cards(1, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="caed74b9-f0e0-53cd-a5aa-837cd01b4fa8",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1", "Alcremie"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Ability(
            title="Sharing Sweets",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have each player draw a card.",
            trigger=Triggers.ON_EVOLVE,
            effect=sharing_sweets,
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
