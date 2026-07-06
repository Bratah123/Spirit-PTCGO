from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d0bac268-9afc-539a-bb81-9147795e0cc5",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    display_name="Inteleon V",
    searchable_by=["Inteleon V", "Basic", "V", "InteleonV"],
    subtypes=["Basic", "V"],
    collector_number=49,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=818,
    abilities=[
        Attack(
            title="Snipe Shot",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Report",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)