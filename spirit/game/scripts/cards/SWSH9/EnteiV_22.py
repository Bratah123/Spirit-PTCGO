from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="71c52931-12f6-506a-86d3-8b8146535f3c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnteiV.Name",
    display_name="Entei V",
    searchable_by=["Entei V", "Basic", "V", "EnteiV"],
    subtypes=["Basic", "V"],
    collector_number=22,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Fleet-Footed",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Burning Rondo",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)