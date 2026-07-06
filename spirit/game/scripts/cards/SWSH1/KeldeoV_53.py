from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b27685d3-902a-5039-8132-7ca8811267d0",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KeldeoV.Name",
    display_name="Keldeo V",
    searchable_by=["Keldeo V", "Basic", "V", "KeldeoV"],
    subtypes=["Basic", "V"],
    collector_number=53,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=647,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Secret Sword",
            game_text="This attack does 30 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)