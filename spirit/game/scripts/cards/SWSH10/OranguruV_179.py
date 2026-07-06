from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b09d0bf8-9921-5aad-a090-0766d88cd682",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OranguruV.Name",
    display_name="Oranguru V",
    searchable_by=["Oranguru V", "Basic", "V", "OranguruV"],
    subtypes=["Basic", "V"],
    collector_number=179,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Ability(
            title="Back Order",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may search your deck for up to 2 Pok\u00e9mon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)