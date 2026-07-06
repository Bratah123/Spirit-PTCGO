from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4357a9e4-cfc0-5a15-9da5-a785f1242b83",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Selickt",
            game_text="Your opponent chooses to discard the top 3 cards of their deck or to discard 3 cards from their hand.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
        Attack(
            title="Pitch",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)