from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
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


card = PokemonCardDef(
    guid="5dca825b-872d-52e4-b840-ce040e058afc",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom", "Stage 2", "Bellossom"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Windmill",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Flower Tornado",
            game_text="Move as many Grass Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=leaf_tornado,
        ),
    ],
)