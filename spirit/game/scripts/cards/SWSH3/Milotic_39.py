from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets, requires_damaged_pokemon


async def bright_heal(ctx):
    if await ctx.ask_yes_no("Heal 20 damage from each of your Pokémon?"):
        await heal_targets(20, "each_own")(ctx)


card = PokemonCardDef(
    guid="d250a912-f03a-555e-a0bc-32b1d3266157",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Bright Heal",
            game_text="Once during your turn, you may heal 20 damage from each of your Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_damaged_pokemon(),
            effect=bright_heal,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)