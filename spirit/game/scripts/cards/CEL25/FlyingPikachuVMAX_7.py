from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3f7a335-9942-5930-9395-5f6d4d26754e",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachuVMAX.Name",
    display_name="Flying Pikachu VMAX",
    searchable_by=["Flying Pikachu VMAX", "VMAX", "FlyingPikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=7,
    set_code="CEL25",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.FlyingPikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Max Balloon",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)