from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.pokemon import energy_provides_type


async def fires_power(ctx):
    """30. If this Pokémon has any Fire Energy, Defending is Burned."""
    await ctx.deal_damage()
    if any(
        energy_provides_type(e, PokemonTypes.FIRE.value)
        for e in ctx.attached_energies(ctx.attacker)
    ):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="da050c61-ae6a-568a-b7b6-6c02f99add87",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage", "Stage 1", "Simisage"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    family_id=511,
    abilities=[
        Attack(
            title="Fire's Power",
            game_text="If this Pok\u00e9mon has any Fire Energy attached to it, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=fires_power,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
