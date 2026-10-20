from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _spreading_flames(ctx):
    """Attach 3 Fire Energy cards from your discard pile to your Pokemon in any way you like."""
    for _ in range(3):
        cards = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
        mine = ctx.my_pokemon_in_play()
        if not cards:
            return
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Fire Energy card")
        if not picks:
            return
        target = mine[0] if len(mine) == 1 else await ctx.choose_pokemon(mine, "Attach it to which Pokémon?")
        await ctx.attach_energy(picks[0], target or mine[0])


card = PokemonCardDef(
    guid="e6f876b7-7964-5511-80c9-1c99a4d44b3e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach 3 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            effect=_spreading_flames,
        ),
        Attack(
            title="Heat Blow",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)