from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28180ee4-5247-514d-94fe-c1a3f9b523ed",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitanVMAX.Name",
    display_name="Galarian Darmanitan VMAX",
    searchable_by=["Galarian Darmanitan VMAX", "VMAX", "GalarianDarmanitanVMAX"],
    subtypes=["VMAX"],
    collector_number=37,
    set_code="SWSH4",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarmanitanV.Name",
    family_id=555,
    abilities=[
        Attack(
            title="Max Whiteout",
            game_text="This attack also does 30 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=200,
            effect=unimplemented,
        ),
    ],
)