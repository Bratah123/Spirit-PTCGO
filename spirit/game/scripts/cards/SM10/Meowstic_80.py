from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.sm3 import perplexing_eyes

async def caturday(ctx):
    """Draw 3 cards. If you do, this Pokemon is now Asleep."""
    drawn = await ctx.draw_cards(3)
    if drawn:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="6e6806fa-14f9-5fdc-84fb-459099d0e9a1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1", "Meowstic"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Attack(
            title="Caturday",
            game_text="Draw 3 cards. If you do, this Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=caturday,
        ),
        Attack(
            title="Perplexing Eyes",
            game_text="The Defending Pok\u00e9mon's Weakness is now Psychic until the end of your next turn. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=perplexing_eyes,
        ),
    ],
)