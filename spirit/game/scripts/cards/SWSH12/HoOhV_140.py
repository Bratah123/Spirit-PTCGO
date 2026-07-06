from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3949c42-5090-52af-9991-9916a3013f65",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhV.Name",
    display_name="Ho-Oh V",
    searchable_by=["Ho-Oh V", "Basic", "V", "HoOhV"],
    subtypes=["Basic", "V"],
    collector_number=140,
    set_code="SWSH12",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Ability(
            title="Reviving Flame",
            game_text="Once during your turn, if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, attach up to 4 basic Energy cards from your discard pile to this Pok\u00e9mon. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="This attack does 30 more damage for each type of basic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)