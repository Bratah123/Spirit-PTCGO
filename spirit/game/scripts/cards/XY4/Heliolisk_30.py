from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _parabolic_spark(ctx):
    """Discard any number of Lightning Energy from your Pokemon: 30 times the
    number of Energy cards discarded."""
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
            if _is_lightning_energy(e)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                   prompt="Discard any number of Lightning Energy") if pool else []
    if picks:
        await ctx.discard_cards(picks)
    await ctx.deal_damage(30 * len(picks or []))


card = PokemonCardDef(
    guid="cfa7d0a2-4c25-5e81-9f0a-3b6c9381ef6e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1", "Heliolisk"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Parabolic Spark",
            game_text="Discard as many Lightning Energy attached to your Pok\u00e9mon as you like. This attack does 30 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=_parabolic_spark,
        ),
    ],
)