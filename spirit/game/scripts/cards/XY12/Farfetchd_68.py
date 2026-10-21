from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="647effbd-8d0b-562f-8c78-62ebcb502159",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=83,
    abilities=[
        Attack(
            title="Leek Slap",
            game_text="This Pok\u00e9mon can't use Leek Slap during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=None,
            locks_next_turn=True,
        ),
        Attack(
            title="Pot Smash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)