from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import takes_less_passive


def _fire_or_water(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types or PokemonTypes.WATER.value in types


card = PokemonCardDef(
    guid="8d06e0be-4251-5a0f-a7d0-271ee1eccb89",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to this Pok\u00e9mon by attacks from your opponent's Fire or Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, attacker_pred=_fire_or_water),
        ),
        Attack(
            title="Rocket Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)