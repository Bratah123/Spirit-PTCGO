from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def _toppling_wind(ctx):
    """On evolve: you may discard the top 3 cards of your opponent's deck."""
    top = ctx.deck_top(3, player_id=ctx.opponent_id)
    if top and await ctx.ask_yes_no("Discard the top 3 cards of your opponent's deck?"):
        await ctx.discard_cards(top)


async def _giga_horn(ctx):
    """Flip 2 coins. If both are tails, this attack does nothing."""
    results = await ctx.flip_coins(2, "Giga Horn")
    if any(results):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="4534801f-0b6a-5ac0-bd18-06d80d259b7b",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=80,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Ability(
            title="Toppling Wind",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may discard the top 3 cards of your opponent's deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=_toppling_wind,
        ),
        Attack(
            title="Giga Horn",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=_giga_horn,
        ),
    ],
)