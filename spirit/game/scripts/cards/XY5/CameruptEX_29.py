from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _explosive_jet(ctx):
    """Discard any number of Fire Energy from your Pokemon: 50 times the
    number of Energy cards discarded."""
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
            if _is_fire_energy(e)]
    picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                   prompt="Discard any number of Fire Energy") if pool else []
    if picks:
        await ctx.discard_cards(picks)
    await ctx.deal_damage(50 * len(picks or []))


card = PokemonCardDef(
    guid="565f2e1e-3ff7-532a-9749-d303a682e74f",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CameruptEX.Name",
    display_name="Camerupt-EX",
    searchable_by=["Camerupt-EX", "Basic", "EX", "CameruptEX"],
    subtypes=["Basic", "EX"],
    collector_number=29,
    set_code="XY5",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=323,
    abilities=[
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Explosive Jet",
            game_text="Discard as many Fire Energy attached to your Pok\u00e9mon as you like. This attack does 50 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=_explosive_jet,
        ),
    ],
)