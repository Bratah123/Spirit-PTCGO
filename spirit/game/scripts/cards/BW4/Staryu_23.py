from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95cd93cd-028c-5f1a-8421-4d34b6e9167a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic", "Staryu"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard an Energy attached to this Pok\u00e9mon and heal all damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)