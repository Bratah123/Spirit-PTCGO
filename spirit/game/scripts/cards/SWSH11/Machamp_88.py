from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f300a416-8ca5-5ebb-b0b0-e2f31615d632",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Crisis Muscles",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon gets +150 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Strong-Arm Lariat",
            game_text="You may do 100 more damage. If you do, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)