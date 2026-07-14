from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


async def cry_of_destruction(ctx):
    """Discard up to 3 Special Energy from your opponent's Pokemon."""
    energies = []
    for pokemon in ctx.opponent_pokemon_in_play():
        if ctx.effects_blocked(pokemon):
            continue
        energies.extend(e for e in ctx.attached_energies(pokemon) if is_special_energy(e))
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, min(3, len(energies)), minimum=0,
        prompt="Discard up to 3 Special Energy from your opponent's Pokémon.",
    )
    await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="904e53b8-7d9f-56b2-9258-ddd922439997",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Cry of Destruction",
            game_text="Discard up to 3 Special Energy from your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=cry_of_destruction,
        ),
        Attack(
            title="Dark Feather",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)