from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1dd90b4-4dd3-5f22-9eb4-3c7b1646ae0c",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowbro.Name",
    display_name="Galarian Slowbro",
    searchable_by=["Galarian Slowbro", "Stage 1", "GalarianSlowbro"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Splattering Poison",
            game_text="Both Active Pok\u00e9mon are now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Unhinged Hammer",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)