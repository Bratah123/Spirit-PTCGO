from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import team_damage_boost_passive


def _is_metal_pokemon(pokemon) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.METAL.value in types


card = PokemonCardDef(
    guid="fd0ba61c-aa8a-55e0-b86f-dfb81bbe22d4",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPerrserker.Name",
    display_name="Galarian Perrserker",
    searchable_by=["Galarian Perrserker", "Stage 1", "GalarianPerrserker"],
    subtypes=["Stage 1"],
    collector_number=205,
    set_code="SWSH2",
    rarity=Rarities.RareSecret,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Steely Spirit",
            game_text="Your Metal Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20, attacker_pred=_is_metal_pokemon),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)