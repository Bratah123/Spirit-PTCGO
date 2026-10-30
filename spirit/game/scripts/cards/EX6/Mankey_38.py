from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import mischief_shuffle

card = PokemonCardDef(
    guid="77aadef6-3938-5a04-b264-b2699936bfeb",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic", "Mankey"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Mischief",
            game_text="Shuffle your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mischief_shuffle(),
        ),
        Attack(
            title="Light Punch",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)