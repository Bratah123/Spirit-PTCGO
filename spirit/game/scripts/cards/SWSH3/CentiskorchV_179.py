from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8585f076-23fd-5257-b0c4-3193697b639b",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    display_name="Centiskorch V",
    searchable_by=["Centiskorch V", "Basic", "V", "CentiskorchV"],
    subtypes=["Basic", "V"],
    collector_number=179,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=851,
    abilities=[
        Attack(
            title="Radiating Heat",
            game_text="You may discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Burning Train",
            cost={PokemonTypes.FIRE: 4},
            damage=180,
        ),
    ],
)