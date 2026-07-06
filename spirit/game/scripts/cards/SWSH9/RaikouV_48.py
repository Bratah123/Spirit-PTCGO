from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3bde83ea-247d-58ca-9c68-7e7796806e9d",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaikouV.Name",
    display_name="Raikou V",
    searchable_by=["Raikou V", "Basic", "V", "RaikouV"],
    subtypes=["Basic", "V"],
    collector_number=48,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Ability(
            title="Fleet-Footed",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Rondo",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)