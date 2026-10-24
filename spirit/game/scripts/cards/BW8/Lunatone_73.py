from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def _premonition(ctx):
    """Look at the top 2 cards of your deck and put them back in any order."""
    await ctx.reorder_deck_top(2)


card = PokemonCardDef(
    guid="71c932b0-ab7d-5e06-aeed-a21dc9a44ca0",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=337,
    abilities=[
        Ability(
            title="Premonition",
            game_text="Once during your turn (before your attack), you may look at the top 2 cards of your deck and put them back on top of your deck in any order.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            effect=_premonition,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)