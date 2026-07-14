from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def extreme_freeze(ctx):
    """Discard any amount of Water Energy from your Pokémon; 60 damage for
    each card discarded this way."""
    candidates = [
        e for p in ctx.my_pokemon_in_play()
        for e in ctx.attached_energies(p)
        if energy_provides_type(e, PokemonTypes.WATER.value)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, len(candidates), minimum=0,
        prompt="Choose any amount of Water Energy to discard",
    )
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="3f309371-5702-5f03-9019-fe2863ce729d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem", "Basic", "Kyurem"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=646,
    abilities=[
        Attack(
            title="Extreme Freeze",
            game_text="Discard any amount of Water Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.METAL: 1},
            damage=60,
            damage_operator="x",
            effect=extreme_freeze,
        ),
    ],
)