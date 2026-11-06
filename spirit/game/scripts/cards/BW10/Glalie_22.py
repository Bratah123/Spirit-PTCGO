from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _reflect_energy(ctx):
    """Printed damage; move a Water Energy from this Pokemon to 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _is_water_energy(e)]
    if not bench or not pool:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
    await ctx.move_energy(pool[0], target or bench[0])


card = PokemonCardDef(
    guid="26d9d2cf-629a-56cb-805f-41146fceca0a",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Team Plasma", "Glalie"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=22,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move a Water Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_reflect_energy,
        ),
    ],
)