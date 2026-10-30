from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import aerowing


card = PokemonCardDef(
    guid="b8503fed-f8fd-5b3c-8275-b16fd2564bc9",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Aerowing",
            game_text="You may flip a coin. If heads, this attack does 80 damage. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            effect=aerowing,
        ),
    ],
)
