from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ddc11dde-ae01-51b7-b894-8ae3e9b8d54b",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Yanmega"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SWSH45",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Nosedive",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)