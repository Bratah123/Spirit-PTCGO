from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import energy_provides_type


async def leaf_tornado(ctx):
    """60 damage, then move Grass Energy freely among your Pokémon."""
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    if len(mine) < 2:
        return
    await ctx.move_energy_freely(
        mine, mine,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.GRASS.value),
        prompt="Choose a Grass Energy to move",
    )


async def _royal_heal(ctx):
    """Between turns: heal 10 damage from each of your Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


card = PokemonCardDef(
    guid="29f0368e-9b76-5191-9be8-eb676410bcf6",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=125,
    set_code="BW6",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=497,
    abilities=[
        Ability(
            title="Royal Heal",
            game_text="At any times between turns, heal 10 damage from each of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=_royal_heal,
        ),
        Attack(
            title="Leaf Tornado",
            game_text="Move as many Grass Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=leaf_tornado,
        ),
    ],
)