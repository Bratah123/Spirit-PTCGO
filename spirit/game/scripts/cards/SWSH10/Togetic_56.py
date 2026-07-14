from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def voice_of_happiness(ctx):
    """On evolve: you may heal 30 damage from your Active Pokémon."""
    active = ctx.my_active()
    if active is None:
        return
    if await ctx.ask_yes_no("Heal 30 damage from your Active Pokémon?"):
        await ctx.heal(30, active)

card = PokemonCardDef(
    guid="3ac6d2dc-03ad-5b33-b2e7-0b25fee6ebd9",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Voice of Happiness",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal 30 damage from your Active Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=voice_of_happiness,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)