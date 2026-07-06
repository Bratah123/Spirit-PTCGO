from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88ac3dc5-9284-5562-84a7-3d908baa2fc5",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmpoleonV.Name",
    display_name="Empoleon V",
    searchable_by=["Empoleon V", "Basic", "V", "Rapid Strike", "EmpoleonV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=146,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=395,
    abilities=[
        Ability(
            title="Emperor's Eyes",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Basic Pok\u00e9mon in play have no Abilities, except for Pok\u00e9mon with a Rule Box (Pok\u00e9mon V, Pok\u00e9mon-GX, etc. have Rule Boxes).",
            effect=unimplemented,
        ),
        Attack(
            title="Swirling Slice",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)