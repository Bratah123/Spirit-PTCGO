from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.support_common import search_to_bench


async def axe_slash(ctx):
    """Discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon."""
    await ctx.deal_damage()
    discarded = await ctx.discard_energy_from(ctx.attacker, 1)
    if not discarded:
        return
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(defender, 1)


from spirit.game.session.effects import is_basic_pokemon


def _basic_fire(card):
    return is_basic_pokemon(card) and PokemonTypes.FIRE.value in (
        card.get_attribute(AttrID.POKEMON_TYPES) or []
    )


card = PokemonCardDef(
    guid="ee8df031-bc12-5795-a3d0-ff67484be0d4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Attack(
            title="Passionate Dance",
            game_text="Search your deck for up to 3 Basic Fire Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=search_to_bench(_basic_fire, count=3, prompt='Choose up to 3 Basic Fire Pokémon'),
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            effect=axe_slash,
        ),
    ],
)