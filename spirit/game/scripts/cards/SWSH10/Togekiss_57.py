from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def shine_of_happiness(ctx):
    """On evolve: you may heal 90 damage from your Active Pokémon."""
    active = ctx.my_active()
    if active is None:
        return
    if await ctx.ask_yes_no("Heal 90 damage from your Active Pokémon?"):
        await ctx.heal(90, active)

card = PokemonCardDef(
    guid="9ae40432-4e80-511c-a9c7-10233a55008c",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Shine of Happiness",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal 90 damage from your Active Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=shine_of_happiness,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)