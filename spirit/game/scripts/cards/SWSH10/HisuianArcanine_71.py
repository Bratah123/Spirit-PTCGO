from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2eb21b94-ae72-50e7-8175-5aff2bcf5ac3",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianArcanine.Name",
    display_name="Hisuian Arcanine",
    searchable_by=["Hisuian Arcanine", "Stage 1", "HisuianArcanine"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Scorching Horn",
            game_text="If this Pok\u00e9mon has any Fire Energy attached, this attack does 80 more damage, and your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)