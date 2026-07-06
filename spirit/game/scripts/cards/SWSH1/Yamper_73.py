from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39c6ff6d-7031-51e2-8ae6-84feab02af01",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    display_name="Yamper",
    searchable_by=["Yamper", "Basic", "Yamper"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=835,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)