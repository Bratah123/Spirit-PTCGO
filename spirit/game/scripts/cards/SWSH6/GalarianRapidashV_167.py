from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="44d23c3a-91a2-58d8-ae6e-0d502fd69bf6",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRapidashV.Name",
    display_name="Galarian Rapidash V",
    searchable_by=["Galarian Rapidash V", "Basic", "V", "GalarianRapidashV"],
    subtypes=["Basic", "V"],
    collector_number=167,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=78,
    abilities=[
        Attack(
            title="Libra Horn",
            game_text="Put damage counters on 1 of your opponent's Pok\u00e9mon until its remaining HP is 100.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)