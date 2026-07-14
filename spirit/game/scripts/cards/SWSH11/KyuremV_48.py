from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.support_common import distribute_energy


def _is_water_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and not is_special_energy(card) and PokemonTypes.WATER.value in types


async def rapid_freeze(ctx):
    """Attach any number of Water Energy cards from your hand to your Pokemon in any way you like."""
    pool = [c for c in ctx.hand() if _is_water_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0, prompt="Choose Water Energy cards to attach")
    if not picks:
        return
    await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


card = PokemonCardDef(
    guid="31832006-11a2-53d0-a709-a3bf0bcefa20",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremV.Name",
    display_name="Kyurem V",
    searchable_by=["Kyurem V", "Basic", "V", "KyuremV"],
    subtypes=["Basic", "V"],
    collector_number=48,
    set_code="SWSH11",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Rapid Freeze",
            game_text="Attach any number of Water Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=rapid_freeze,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 3},
            damage=140,
        ),
    ],
)