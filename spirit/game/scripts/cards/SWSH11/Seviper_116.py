from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1dc3ce1-d055-5cf0-a510-ede30fc3df28",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic", "Seviper"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=336,
    abilities=[
        Attack(
            title="Sucker Punch and Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Darkness Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)