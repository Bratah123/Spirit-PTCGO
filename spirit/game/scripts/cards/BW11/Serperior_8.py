from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import energy_provides_type


async def royal_heal(ctx):
    """Between turns: heal 10 damage from each of your Pokémon."""
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10, pokemon)


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


card = PokemonCardDef(
    guid="6daf14be-98a7-50f3-912f-657434e1c4ea",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Royal Heal",
            game_text="At any time between turns, heal 10 damage from each of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=royal_heal,
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
