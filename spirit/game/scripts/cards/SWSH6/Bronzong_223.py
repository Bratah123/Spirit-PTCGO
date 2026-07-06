from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="df6b4ac1-746d-514f-b8c5-02172778513b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=223,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=437,
    abilities=[
        Ability(
            title="Metal Transfer",
            game_text="As often as you like during your turn, you may move a Metal Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)