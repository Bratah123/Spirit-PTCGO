from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cc16986-3a72-5156-9262-6ee2d092a4a1",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If this Pok\u00e9mon has any Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Tiny Charge",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)