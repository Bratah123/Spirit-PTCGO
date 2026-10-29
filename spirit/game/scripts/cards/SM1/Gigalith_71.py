from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


def _is_fighting_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def _rock_artillery(ctx):
    """Discard any amount of Fighting Energy from your Pokemon; 50 per card."""
    energies = [e for p in ctx.my_pokemon_in_play()
                for e in ctx.attached_energies(p) if _is_fighting_energy(e)]
    picks = []
    if energies:
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Choose any amount of Fighting Energy to discard from your Pokémon.")
    if picks:
        await ctx.discard_cards(picks)
        await ctx.deal_damage(50 * len(picks))


card = PokemonCardDef(
    guid="b7117b1e-af9d-5fa7-9352-7bb115870442",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=71,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Rock Artillery",
            game_text="Discard any amount of Fighting Energy from your Pok\u00e9mon. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=_rock_artillery,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=feint,
        ),
    ],
)