from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def frozen_heat(ctx):
    water_energy = [e for e in ctx.attached_energies(ctx.attacker)
                    if energy_provides_type(e, PokemonTypes.WATER.value)]
    bonus = 0
    if water_energy and await ctx.ask_yes_no(
            "Discard all Water Energy from this Pokémon?"):
        await ctx.discard_energy_from(
            ctx.attacker, 99,
            predicate=lambda c: energy_provides_type(c, PokemonTypes.WATER.value),
        )
        bonus = 60
    await ctx.deal_damage(110 + bonus)


card = PokemonCardDef(
    guid="7c757cda-c44f-5d82-871d-5a2df8fb6b04",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitan.Name",
    display_name="Galarian Darmanitan",
    searchable_by=["Galarian Darmanitan", "Stage 1", "GalarianDarmanitan"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Frozen Heat",
            game_text="You may discard all Water Energy from this Pok\u00e9mon. If you do, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            effect=frozen_heat,
        ),
    ],
)