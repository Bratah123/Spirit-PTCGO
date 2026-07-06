from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6c0f065a-501e-5654-9942-b3dc7897c827",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    display_name="Mareanie",
    searchable_by=["Mareanie", "Basic", "Mareanie"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=747,
    abilities=[
        Attack(
            title="Regeneration",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Poison Tentacles",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)