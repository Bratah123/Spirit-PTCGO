from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98101893-57f5-5813-9984-cc2ebe838ffa",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultV.Name",
    display_name="Dragapult V",
    searchable_by=["Dragapult V", "Basic", "V", "DragapultV"],
    subtypes=["Basic", "V"],
    collector_number=92,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=887,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Jet Assault",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)