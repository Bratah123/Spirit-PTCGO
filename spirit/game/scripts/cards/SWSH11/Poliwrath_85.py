from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def splash_loop(ctx):
    """160. Put 2 Energy attached to this Pokémon into your hand."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.source)
    if not energies:
        return
    count = min(2, len(energies))
    picks = await ctx.choose_cards(
        energies, count, minimum=count,
        prompt="Choose Energy to put into your hand",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="cfd4bfd0-7fbb-556d-a67d-41323c344d6d",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Split Spiral Punch",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Splash Loop",
            game_text="Put 2 Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=splash_loop,
        ),
    ],
)