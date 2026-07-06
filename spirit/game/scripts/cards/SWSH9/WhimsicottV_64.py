from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b1665e3-c8dc-5143-8894-199d40a96cfa",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottV.Name",
    display_name="Whimsicott V",
    searchable_by=["Whimsicott V", "Basic", "V", "WhimsicottV"],
    subtypes=["Basic", "V"],
    collector_number=64,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=547,
    abilities=[
        Attack(
            title="Fluff Gets in the Way",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Cotton Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)