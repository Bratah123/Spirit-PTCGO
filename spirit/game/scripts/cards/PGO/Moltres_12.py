from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.passives_common import team_damage_boost_passive


def _flare_symbol_attacker(pokemon) -> bool:
    if not is_basic_pokemon(pokemon):
        return False
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.FIRE.value not in types:
        return False
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", None) or ""
    return name != "Moltres"


card = PokemonCardDef(
    guid="b3cf08b6-fbf4-5c63-ad13-b353e030ec75",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Flare Symbol",
            game_text="Your Basic Fire Pok\u00e9mon's attacks, except any Moltres, do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(10, attacker_pred=_flare_symbol_attacker),
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)