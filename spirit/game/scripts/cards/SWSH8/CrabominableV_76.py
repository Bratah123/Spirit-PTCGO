from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca1238a6-159b-5f03-a953-35e85cbb263e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrabominableV.Name",
    display_name="Crabominable V",
    searchable_by=["Crabominable V", "Basic", "V", "CrabominableV"],
    subtypes=["Basic", "V"],
    collector_number=76,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    family_id=740,
    abilities=[
        Attack(
            title="Trigger Avalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Destroyer Punch",
            game_text="This attack does 60 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)