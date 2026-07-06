from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43be4010-a927-5e00-9489-9b5eac6c9ae7",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylV.Name",
    display_name="Aerodactyl V",
    searchable_by=["Aerodactyl V", "Basic", "V", "AerodactylV"],
    subtypes=["Basic", "V"],
    collector_number=179,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=142,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Rock Crush",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)