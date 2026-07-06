from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b370c27e-c08b-5d0f-ab21-42fafe1a3e32",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    display_name="Zacian V",
    searchable_by=["Zacian V", "Basic", "V", "ZacianV"],
    subtypes=["Basic", "V"],
    collector_number=138,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Ability(
            title="Intrepid Sword",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and attach any number of Metal Energy cards you find there to this Pok\u00e9mon. Put the other cards into your hand. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Brave Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 3},
            damage=230,
            effect=unimplemented,
        ),
    ],
)