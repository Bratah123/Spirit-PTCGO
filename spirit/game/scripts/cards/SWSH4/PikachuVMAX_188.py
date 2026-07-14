from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def g_max_volt_tackle(ctx):
    energies = ctx.attached_energies(ctx.attacker)
    if energies and await ctx.ask_yes_no(
        "Discard all Energy from this Pokémon? If you do, this attack does 150 more damage."
    ):
        await ctx.discard_energy_from(ctx.attacker, 99)
        await ctx.deal_damage(270)
    else:
        await ctx.deal_damage(120)


card = PokemonCardDef(
    guid="d329c902-ea8a-567e-98ba-e38f005a42cc",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVMAX.Name",
    display_name="Pikachu VMAX",
    searchable_by=["Pikachu VMAX", "VMAX", "PikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=188,
    set_code="SWSH4",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="G-Max Volt Tackle",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 150 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            damage_operator="+",
            effect=g_max_volt_tackle,
        ),
    ],
)