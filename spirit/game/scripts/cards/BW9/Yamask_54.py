from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22210a73-0915-5b67-81a1-e4206f9f54cb",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=562,
    abilities=[
        Attack(
            title="Transfer Pain",
            game_text="Move 1 damage counter from any of your Pok\u00e9mon to any of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)