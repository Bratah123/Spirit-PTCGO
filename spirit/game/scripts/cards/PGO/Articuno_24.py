from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import team_damage_boost_passive
from spirit.game.session.effects import is_basic_pokemon, is_water_pokemon


def _ice_symbol_attacker(pokemon):
    if not (is_basic_pokemon(pokemon) and is_water_pokemon(pokemon)):
        return False
    definition = def_for(pokemon.archetype_id)
    return getattr(definition, "display_name", "") != "Articuno"

card = PokemonCardDef(
    guid="cde48857-1d2a-5303-8d56-23de5aba41b2",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Ice Symbol",
            game_text="Your Basic Water Pok\u00e9mon's attacks, except any Articuno, do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(10, attacker_pred=_ice_symbol_attacker),
        ),
        Attack(
            title="Freezing Wind",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)