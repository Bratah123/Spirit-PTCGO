from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def moonglow_reverse(ctx):
    """Move 2 damage counters from each of your Pokémon to 1 of your
    opponent's Pokémon."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    dest = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if dest is None:
        return
    for source in ctx.my_pokemon_in_play():
        await ctx.move_damage_counters(source, dest, max_count=2)


card = PokemonCardDef(
    guid="0609741e-143a-539a-a387-c5c750f1ee6e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=488,
    abilities=[
        Attack(
            title="Moonglow Reverse",
            game_text="Move 2 damage counters from each of your Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=moonglow_reverse,
        ),
        Attack(
            title="Lunar Blast",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)