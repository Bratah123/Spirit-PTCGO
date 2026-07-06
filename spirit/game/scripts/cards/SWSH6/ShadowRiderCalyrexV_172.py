from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8a7cf595-4e42-53e2-a0cc-4231602dbaa6",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name",
    display_name="Shadow Rider Calyrex V",
    searchable_by=["Shadow Rider Calyrex V", "Basic", "V", "ShadowRiderCalyrexV"],
    subtypes=["Basic", "V"],
    collector_number=172,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=898,
    abilities=[
        Attack(
            title="Shadow Mist",
            game_text="During your opponent's next turn, they can't play any Special Energy or Stadium cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Astral Barrage",
            game_text="Choose 2 of your opponent's Pok\u00e9mon and put 5 damage counters on each of them.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)