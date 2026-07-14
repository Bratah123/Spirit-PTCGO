from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


def _is_grass_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.GRASS.value in types


async def pack_call(ctx):
    going_second = ctx.player_id != ctx.session.first_player_id
    count = 3 if going_second and ctx.session.turn_state.turn_number == 2 else 1
    picks = await ctx.search_deck(
        _is_grass_pokemon, count=count, minimum=0,
        prompt=f"Choose up to {count} Grass Pokémon.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="82a37832-8311-5ff3-8dd9-f1d31cea3047",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Pack Call",
            game_text="Search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. If you go second and it's your first turn, search for up to 3 Grass Pok\u00e9mon instead of 1. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=pack_call,
        ),
        Attack(
            title="Repeated Whip",
            game_text="This attack does 20 more damage for each Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.GRASS), 20, base=60),
        ),
    ],
)