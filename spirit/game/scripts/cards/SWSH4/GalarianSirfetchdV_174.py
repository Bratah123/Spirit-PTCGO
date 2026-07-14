from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def resolute_spear(ctx):
    """Once per turn, on move to Active: you may move any amount of Fighting Energy from your other Pokemon to it."""
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
    if not any(energy_provides_type(e, PokemonTypes.FIGHTING.value)
               for p in others for e in ctx.attached_energies(p)):
        return
    if not await ctx.ask_yes_no("Move any amount of Fighting Energy from your other Pokémon to this Pokémon?"):
        return
    await ctx.move_energy_freely(
        others, [ctx.source],
        predicate=lambda e: energy_provides_type(e, PokemonTypes.FIGHTING.value),
    )


card = PokemonCardDef(
    guid="af771144-e039-53ec-9841-3786dfdee175",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSirfetchdV.Name",
    display_name="Galarian Sirfetch'd V",
    searchable_by=["Galarian Sirfetch'd V", "Basic", "V", "GalarianSirfetchdV"],
    subtypes=["Basic", "V"],
    collector_number=174,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=865,
    abilities=[
        Ability(
            title="Resolute Spear",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may move any amount of Fighting Energy from your other Pok\u00e9mon to it.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=resolute_spear,
        ),
        Attack(
            title="Meteor Smash",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            locks_next_turn=True,
        ),
    ],
)