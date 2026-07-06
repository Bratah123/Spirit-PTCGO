from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="baacab2c-1b95-548b-8843-dca3c64fba18",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    display_name="Rookidee",
    searchable_by=["Rookidee", "Basic", "Rookidee"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=821,
    abilities=[
        Attack(
            title="Pluck",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)