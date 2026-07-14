from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def psy_purge(ctx):
    energies = [
        e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
        if energy_provides_type(e, PokemonTypes.PSYCHIC.value)
    ]
    picks = await ctx.choose_cards(
        energies, 3, minimum=0,
        prompt="Discard up to 3 Psychic Energy from your Pokémon.",
    )
    await ctx.discard_cards(picks)
    if picks:
        await ctx.deal_damage(90 * len(picks))


async def star_raid(ctx):
    for pokemon in ctx.opponent_pokemon_in_play():
        if is_pokemon_v(pokemon.archetype_id):
            await ctx.deal_damage(120, target=pokemon, apply_modifiers=False)


card = PokemonCardDef(
    guid="54612974-e4ee-5bff-86c8-fb5a59135b84",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVSTAR.Name",
    display_name="Mewtwo VSTAR",
    searchable_by=["Mewtwo VSTAR", "VSTAR", "MewtwoVSTAR"],
    subtypes=["VSTAR"],
    collector_number=86,
    set_code="PGO",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoV.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Psy Purge",
            game_text="Discard up to 3 Psychic Energy from your Pok\u00e9mon. This attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=psy_purge,
        ),
        Attack(
            title="Star Raid",
            game_text="This attack does 120 damage to each of your opponent's Pok\u00e9mon V. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            vstar=True,
            effect=star_raid,
        ),
    ],
)