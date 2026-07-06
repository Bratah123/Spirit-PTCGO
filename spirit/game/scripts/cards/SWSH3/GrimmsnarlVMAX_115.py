from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ece27e6b-f231-58a3-ad29-8d5c8e8e27d3",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlVMAX.Name",
    display_name="Grimmsnarl VMAX",
    searchable_by=["Grimmsnarl VMAX", "VMAX", "GrimmsnarlVMAX"],
    subtypes=["VMAX"],
    collector_number=115,
    set_code="SWSH3",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    family_id=861,
    abilities=[
        Attack(
            title="G-Max Drill",
            game_text="This attack does 50 more damage for each extra Darkness Energy attached to this Pok\u00e9mon (in addition to this attack's cost). You can't add more than 100 damage in this way.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=170,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)