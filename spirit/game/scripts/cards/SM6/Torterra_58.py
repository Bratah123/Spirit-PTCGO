from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import earthquake

async def gulp_down(ctx):
    """Heal from this Pokémon the same amount of damage you did to your
    opponent's Active Pokémon."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)

card = PokemonCardDef(
    guid="a5a040b6-2d78-5776-a52d-a261c7f5013a",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name",
    display_name="Torterra",
    searchable_by=["Torterra", "Stage 2", "Torterra"],
    subtypes=["Stage 2"],
    collector_number=58,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=389,
    abilities=[
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=gulp_down,
        ),
        Attack(
            title="Earthquake",
            game_text="This attack does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=earthquake,
        ),
    ],
)
