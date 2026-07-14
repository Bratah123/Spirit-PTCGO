from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, defender_is_v
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy


def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def spreading_flames(ctx):
    """Attach up to 3 Fire Energy cards from your discard pile to your
    Pokemon, any way you like."""
    cards = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 3, minimum=0,
        prompt="Choose up to 3 Fire Energy cards from your discard pile to attach.",
    )
    if not picks:
        return
    candidates = ctx.my_pokemon_in_play()
    if not candidates:
        return
    await distribute_energy(ctx, picks, candidates)


card = PokemonCardDef(
    guid="03ce083f-0c51-57cb-a688-1267edd478f5",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniVMAX.Name",
    display_name="Victini VMAX",
    searchable_by=["Victini VMAX", "VMAX", "VictiniVMAX"],
    subtypes=["VMAX"],
    collector_number=165,
    set_code="SWSH5",
    rarity=Rarities.RareRainbow,
    hp=310,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    family_id=494,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach up to 3 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=spreading_flames,
        ),
        Attack(
            title="Max Victory",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 120 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(defender_is_v, 120),
        ),
    ],
)