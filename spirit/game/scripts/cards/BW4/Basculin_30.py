from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="215e9a76-61a5-5661-884e-a71f402f7000",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name",
    display_name="Basculin",
    searchable_by=["Basculin", "Basic", "Basculin"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Bared Fangs",
            game_text="If, before this Pok\u00e9mon does damage, the Defending Pok\u00e9mon has no damage counters on it, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)