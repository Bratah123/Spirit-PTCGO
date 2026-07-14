from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def vital_powder(ctx):
    """Heal all damage from 2 of your Benched Pokémon."""
    bench = ctx.my_bench()
    if not bench:
        return
    picks = await ctx.choose_cards(
        bench, 2, prompt="Choose 2 Benched Pokémon to heal"
    )
    for pokemon in picks:
        heal_amount = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if heal_amount > 0:
            await ctx.heal(heal_amount, pokemon)

card = PokemonCardDef(
    guid="059e1647-e553-54bc-9375-392956f1a637",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Vital Powder",
            game_text="Heal all damage from 2 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=vital_powder,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)