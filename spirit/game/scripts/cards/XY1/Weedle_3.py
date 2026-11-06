from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is


def _is_grass(pokemon):
    return PokemonTypes.GRASS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="8fe73a37-91a0-521f-9feb-36df35f29a1b",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Leaf Munch",
            game_text="If your opponent's Active Pok\u00e9mon is a Grass Pok\u00e9mon, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(active_is(_is_grass), 20, base=10),
        ),
    ],
)