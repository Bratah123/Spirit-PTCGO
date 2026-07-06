from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab662183-4c5a-5ed3-b7c3-614ad592e4b4",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxVMAX.Name",
    display_name="Snorlax VMAX",
    searchable_by=["Snorlax VMAX", "VMAX", "SnorlaxVMAX"],
    subtypes=["VMAX"],
    collector_number=206,
    set_code="SWSH1",
    rarity=Rarities.RareRainbow,
    hp=340,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxV.Name",
    family_id=143,
    abilities=[
        Attack(
            title="G-Max Fall",
            game_text="This attack does 30 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)