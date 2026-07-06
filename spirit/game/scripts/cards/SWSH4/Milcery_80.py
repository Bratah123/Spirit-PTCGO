from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d3ae574-fc82-51eb-8085-9b75ed33f20f",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    display_name="Milcery",
    searchable_by=["Milcery", "Basic", "Milcery"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=868,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Heal 20 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)