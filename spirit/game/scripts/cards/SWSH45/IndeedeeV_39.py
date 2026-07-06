from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37c796ee-50cb-53c9-9088-6214e2371282",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IndeedeeV.Name",
    display_name="Indeedee V",
    searchable_by=["Indeedee V", "Basic", "V", "IndeedeeV"],
    subtypes=["Basic", "V"],
    collector_number=39,
    set_code="SWSH45",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=876,
    abilities=[
        Ability(
            title="Watch Over",
            game_text="Once during your turn, you may heal 20 damage from your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 60 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)