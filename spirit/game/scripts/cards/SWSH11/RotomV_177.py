from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4cb2dd9d-aa7a-536f-8d31-40135a080fd9",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name",
    display_name="Rotom V",
    searchable_by=["Rotom V", "Basic", "V", "RotomV"],
    subtypes=["Basic", "V"],
    collector_number=177,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Instant Charge",
            game_text="Once during your turn, you may draw 3 cards. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Scrap Short",
            game_text="Put any number of Pok\u00e9mon Tool cards from your discard pile in the Lost Zone. This attack does 40 more damage for each card you put in the Lost Zone in this way.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)