from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3089734-e05b-51c2-934e-787d332ce082",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GolurkV.Name",
    display_name="Golurk V",
    searchable_by=["Golurk V", "Basic", "V", "Single Strike", "GolurkV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=70,
    set_code="SWSH7",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=623,
    abilities=[
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Rewind Beam",
            game_text="If your opponent's Active Pok\u00e9mon is an evolved Pok\u00e9mon, devolve it by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=unimplemented,
        ),
    ],
)