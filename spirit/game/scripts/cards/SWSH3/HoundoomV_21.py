from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b5390f15-4b6f-521f-8da2-e26b96f23813",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomV.Name",
    display_name="Houndoom V",
    searchable_by=["Houndoom V", "Basic", "V", "HoundoomV"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=229,
    abilities=[
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Vengeful Flame",
            game_text="If your Benched Fire Pok\u00e9mon have any damage counters on them, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)