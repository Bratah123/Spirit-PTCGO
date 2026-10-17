from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01dbd962-7550-5ccd-a98f-6be0ea892ba9",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Terrakion.Name",
    display_name="Terrakion",
    searchable_by=["Terrakion", "Basic", "Terrakion"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=639,
    abilities=[
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Sacred Sword",
            game_text="This Pok\u00e9mon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            locks_next_turn=True,
        ),
    ],
)
