from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77d75767-1459-549f-bde4-21be6b7328bb",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarV.Name",
    display_name="Tyranitar V",
    searchable_by=["Tyranitar V", "Basic", "V", "TyranitarV"],
    subtypes=["Basic", "V"],
    collector_number=158,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=248,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.DARKNESS: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)