from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="c6c48a11-495f-56ed-92a6-4e718cf763cd",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=83,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Leek Jab",
            game_text="This attack can't be used during your next turn. (Benching Farfetch'd ends this effect.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            locks_next_turn=True,
        ),
    ],
)
