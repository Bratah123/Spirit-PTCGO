from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import ability_lock_passive, is_in_active_spot
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


def _barricaded(pokemon, carrier):
    """While this Pokemon is your Active, non-Psychic Pokemon have no Abilities."""
    me = carrier_pokemon(carrier)
    if me is None or not is_in_active_spot(me):
        return False
    return PokemonTypes.PSYCHIC.value not in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="2c947978-25c2-58b4-8ed6-65c29964defd",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Bide Barricade",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, each Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities (except for Psychic Pok\u00e9mon).",
            passive=ability_lock_passive(_barricaded),
        ),
        Attack(
            title="Psychic Assault",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on('defender'), 10, base=10),
        ),
    ],
)