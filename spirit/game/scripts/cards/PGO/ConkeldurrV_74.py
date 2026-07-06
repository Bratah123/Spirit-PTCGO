from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6cded83-22e8-57ab-bae6-f51a1a627c0e",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ConkeldurrV.Name",
    display_name="Conkeldurr V",
    searchable_by=["Conkeldurr V", "Basic", "V", "ConkeldurrV"],
    subtypes=["Basic", "V"],
    collector_number=74,
    set_code="PGO",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=534,
    abilities=[
        Attack(
            title="Counter",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 90 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)