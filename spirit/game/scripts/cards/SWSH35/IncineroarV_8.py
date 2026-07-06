from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85c3c274-ebeb-55ba-9399-6d0464feb806",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IncineroarV.Name",
    display_name="Incineroar V",
    searchable_by=["Incineroar V", "Basic", "V", "IncineroarV"],
    subtypes=["Basic", "V"],
    collector_number=8,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=727,
    abilities=[
        Attack(
            title="Grand Flame",
            game_text="Attach up to 2 Fire Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Flare Blitzer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)