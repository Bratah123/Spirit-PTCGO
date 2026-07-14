from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_psychic_energy(card):
    return is_basic_energy_card(card) and \
        energy_provides_type(card, PokemonTypes.PSYCHIC.value)


async def adornment(ctx):
    """For each Benched Pokemon, search a Psychic Energy onto it; shuffle."""
    for pokemon in list(ctx.my_bench()):
        definition = def_for(pokemon.archetype_id)
        name = getattr(definition, "display_name", None) or "your Benched Pokémon"
        picks = await ctx.search_deck(
            _is_psychic_energy, count=1, minimum=0,
            prompt=f"Choose a Psychic Energy card to attach to {name}.",
        )
        if picks:
            if pokemon.entity_id not in ctx.visual_targets:
                ctx.visual_targets.append(pokemon.entity_id)
            await ctx.attach_energy(picks[0], pokemon)
    await ctx.shuffle_deck()


async def g_max_whisk(ctx):
    """Discard any amount of Energy from your Pokemon; 60 per card discarded."""
    energies = [e for p in ctx.my_pokemon_in_play()
                for e in ctx.attached_energies(p)]
    picks = []
    if energies:
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Choose any amount of Energy to discard from your Pokémon.",
        )
    if picks:
        await ctx.discard_cards(picks)
        await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="0d0d5da2-bd80-5a43-a206-743b2d8c18f4",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlcremieVMAX.Name",
    display_name="Alcremie VMAX",
    searchable_by=["Alcremie VMAX", "VMAX", "AlcremieVMAX"],
    subtypes=["VMAX"],
    collector_number=73,
    set_code="SWSH45",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlcremieV.Name",
    family_id=869,
    abilities=[
        Attack(
            title="Adornment",
            game_text="For each of your Benched Pokémon, search your deck for a Psychic Energy card and attach it to that Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=adornment,
        ),
        Attack(
            title="G-Max Whisk",
            game_text="Discard any amount of Energy from your Pokémon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="x",
            effect=g_max_whisk,
        ),
    ],
)
