from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7d4930b-3cf6-523b-bf3d-1d798f444bfb",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    display_name="Sandygast",
    searchable_by=["Sandygast", "Basic", "Sandygast"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=769,
    abilities=[
        Attack(
            title="Sneaky Placement",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)