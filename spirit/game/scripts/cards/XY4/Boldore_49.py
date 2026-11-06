from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _core_heal(ctx):
    """Discard a Fighting Energy attached to this Pokemon and heal 50 damage from it."""
    await ctx.discard_energy_from(ctx.attacker, 1, predicate=_is_fighting_energy,
                                  minimum=1, prompt="Discard a Fighting Energy")
    await ctx.heal(50, ctx.attacker)


card = PokemonCardDef(
    guid="d082fc28-b792-5ada-90c7-8bb2219fccd1",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    display_name="Boldore",
    searchable_by=["Boldore", "Stage 1", "Boldore"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Core Heal",
            game_text="Discard a Fighting Energy attached to this Pok\u00e9mon and heal 50 damage from it.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=_core_heal,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 3},
            damage=60,
        ),
    ],
)