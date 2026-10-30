from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import aerowing_optional_flip


card = PokemonCardDef(
    guid="a16581b3-fcc8-51e0-a892-2aaa46c02413",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=249,
    abilities=[
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Aerowing",
            game_text="Before doing damage, you may flip a coin. If tails, this attack does nothing. If heads, this attack does 60 damage instead.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=aerowing_optional_flip(30, 60),
        ),
    ],
)
