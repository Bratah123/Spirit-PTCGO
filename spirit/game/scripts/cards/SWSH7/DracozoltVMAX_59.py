from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5b7b04b5-a3c5-5ccd-ba18-94478c957ca6",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DracozoltVMAX.Name",
    display_name="Dracozolt VMAX",
    searchable_by=["Dracozolt VMAX", "VMAX", "DracozoltVMAX"],
    subtypes=["VMAX"],
    collector_number=59,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DracozoltV.Name",
    family_id=880,
    abilities=[
        Attack(
            title="Spark Trap",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 12 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Max Impact",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
        ),
    ],
)