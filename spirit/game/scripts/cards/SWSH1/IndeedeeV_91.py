from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def watch_over(ctx):
    """Once during your turn, you may heal 20 damage from your Active Pokémon."""
    if await ctx.ask_yes_no("Heal 20 damage from your Active Pokémon?"):
        await ctx.heal(20)


card = PokemonCardDef(
    guid="d079a361-f311-580b-8efc-62acca8e08af",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IndeedeeV.Name",
    display_name="Indeedee V",
    searchable_by=["Indeedee V", "Basic", "V", "IndeedeeV"],
    subtypes=["Basic", "V"],
    collector_number=91,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Ability(
            title="Watch Over",
            game_text="Once during your turn, you may heal 20 damage from your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=watch_over,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 60 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 60, base=10),
        ),
    ],
)