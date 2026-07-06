from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37b9aee1-cc00-5bcd-aeee-e25b288527bd",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name",
    display_name="Drapion",
    searchable_by=["Drapion", "Stage 1", "Drapion"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    family_id=451,
    abilities=[
        Attack(
            title="Hard Press",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
        Attack(
            title="Toxic Strike",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)