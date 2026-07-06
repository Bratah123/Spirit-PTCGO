from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8a067a01-2707-5a82-856e-6f70a811dfa4",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    display_name="Sandygast",
    searchable_by=["Sandygast", "Basic", "Sandygast"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=769,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)