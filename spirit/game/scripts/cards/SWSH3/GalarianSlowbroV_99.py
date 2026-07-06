from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b18af02-c73b-5603-a12e-195280311ac7",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowbroV.Name",
    display_name="Galarian Slowbro V",
    searchable_by=["Galarian Slowbro V", "Basic", "V", "GalarianSlowbroV"],
    subtypes=["Basic", "V"],
    collector_number=99,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=80,
    abilities=[
        Ability(
            title="Rapid-Fire Poison",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may make your opponent's Active Pok\u00e9mon Poisoned.",
            effect=unimplemented,
        ),
        Attack(
            title="Tripping Shot",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)