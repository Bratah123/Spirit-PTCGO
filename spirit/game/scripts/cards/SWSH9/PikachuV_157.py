from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def lightning_blast(ctx):
    lightning_energy = [
        e for e in ctx.attached_energies(ctx.attacker)
        if energy_provides_type(e, PokemonTypes.LIGHTNING.value)
    ]
    if lightning_energy and await ctx.ask_yes_no(
        "Discard all Lightning Energy from this Pokémon? "
        "If you do, this attack does 120 more damage."
    ):
        await ctx.discard_energy_from(
            ctx.attacker, 99,
            predicate=lambda c: energy_provides_type(c, PokemonTypes.LIGHTNING.value),
        )
        await ctx.deal_damage(220)
    else:
        await ctx.deal_damage(100)


card = PokemonCardDef(
    guid="9c07dc16-7be2-52f1-b87a-160772d76404",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=157,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Lightning Blast",
            game_text="You may discard all Lightning Energy from this Pok\u00e9mon. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=lightning_blast,
        ),
    ],
)