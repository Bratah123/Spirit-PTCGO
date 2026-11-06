from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _magma_mantle(ctx):
    """30; you may discard the top card of your deck. If it is a Fire Energy
    card, this attack does 50 more damage."""
    bonus = 0
    top = ctx.deck_top(1)
    if top and await ctx.ask_yes_no("Discard the top card of your deck?"):
        card = top[0]
        await ctx.discard_cards([card])
        if is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value):
            bonus = 50
    await ctx.deal_damage(30 + bonus)


card = PokemonCardDef(
    guid="06d26f02-9385-56ba-900d-af1758c5f8e8",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Magma Mantle",
            game_text="You may discard the top card of your deck. If that card is a Fire Energy card, this attack does 50 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_magma_mantle,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)