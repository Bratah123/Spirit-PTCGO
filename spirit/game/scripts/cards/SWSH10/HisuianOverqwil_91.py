from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5de5d4a-5604-5394-a129-80c522af8ded",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianOverqwil.Name",
    display_name="Hisuian Overqwil",
    searchable_by=["Hisuian Overqwil", "Stage 1", "HisuianOverqwil"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianQwilfish.Name",
    family_id=211,
    abilities=[
        Attack(
            title="Dirty Press",
            game_text="If you have at least 3 Darkness Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)